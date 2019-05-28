#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Integration tests for Flask-Redis."""

import flask
import pytest

from flask_redis import client as uut


@pytest.fixture
def app():
    return flask.Flask(__name__)


def test_constructor(app):
    """Test that a constructor with app instance will initialize the
    connection"""
    redis = uut.FlaskRedis(app)
    assert redis._redis_client is not None
    assert hasattr(redis._redis_client, "connection_pool")


def test_init_app(app):
    """Test that a constructor without app instance will not initialize the
    connection.

    After FlaskRedis.init_app(app) is called, the connection will be
    initialized."""
    redis = uut.FlaskRedis()
    assert redis._redis_client is None
    redis.init_app(app)
    assert redis._redis_client is not None
    assert hasattr(redis._redis_client, "connection_pool")
    if hasattr(app, "extensions"):
        assert "redis" in app.extensions
        assert app.extensions["redis"] == redis


def test_custom_prefix(app):
    """Test that config prefixes enable distinct connections"""
    app.config["DBA_URL"] = "redis://localhost:6379/1"
    app.config["DBB_URL"] = "redis://localhost:6379/2"
    redis_a = uut.FlaskRedis(app, config_prefix="DBA")
    redis_b = uut.FlaskRedis(app, config_prefix="DBB")
    assert redis_a.connection_pool.connection_kwargs["db"] == 1
    assert redis_b.connection_pool.connection_kwargs["db"] == 2


@pytest.mark.parametrize(
    ["strict_flag", "allowed_names"],
    [
        [
            True,
            # StrictRedis points to Redis in newer versions
            {"Redis", "StrictRedis"},
        ],
        [False, {"Redis"}],
    ],
)
def test_strict_parameter(app, strict_flag, allowed_names):
    """Test that initializing with the strict parameter set to True will use
    StrictRedis, and that False will keep using the old Redis class."""

    redis = uut.FlaskRedis(app, strict=strict_flag)
    assert redis._redis_client is not None
    assert type(redis._redis_client).__name__ in allowed_names


def test_custom_provider(app):
    """Test that FlaskRedis can be instructed to use a different Redis client,
    like StrictRedis"""

    class FakeProvider(object):
        @classmethod
        def from_url(cls, *args, **kwargs):
            return cls()

    redis = uut.FlaskRedis.from_custom_provider(FakeProvider)
    assert redis._redis_client is None
    redis.init_app(app)
    assert redis._redis_client is not None
    assert isinstance(redis._redis_client, FakeProvider)
