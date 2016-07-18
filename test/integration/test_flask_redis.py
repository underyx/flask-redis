#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Integration tests for Flask-Redis."""

import flask
from flask_redis import FlaskRedis
import pytest


@pytest.fixture
def app():
    return flask.Flask(__name__)


def test_constructor(app):
    """Test that a constructor with app instance will initialize the
    connection"""
    redis = FlaskRedis(app)
    assert redis._redis_client is not None
    assert hasattr(redis._redis_client, 'connection_pool')


def test_init_app(app):
    """Test that a constructor without app instance will not initialize the
    connection.

    After FlaskRedis.init_app(app) is called, the connection will be
    initialized."""
    redis = FlaskRedis()
    assert redis._redis_client is None
    redis.init_app(app)
    assert redis._redis_client is not None
    assert hasattr(redis._redis_client, 'connection_pool')


def test_custom_prefix(app):
    """Test that config prefixes enable distinct connections"""
    app.config['DBA_URL'] = 'redis://localhost:6379/1'
    app.config['DBB_URL'] = 'redis://localhost:6379/2'
    redis_a = FlaskRedis(app, config_prefix='DBA')
    redis_b = FlaskRedis(app, config_prefix='DBB')
    assert redis_a.connection_pool.connection_kwargs['db'] == 1
    assert redis_b.connection_pool.connection_kwargs['db'] == 2


def test_strict_parameter(app):
    """Test that initializing with the strict parameter set to True will use
    StrictRedis, and that False will keep using the old Redis class."""

    redis = FlaskRedis(app, strict=True)
    assert redis._redis_client is not None
    assert type(redis._redis_client).__name__ == 'StrictRedis'

    redis = FlaskRedis(app, strict=False)
    assert redis._redis_client is not None
    assert type(redis._redis_client).__name__ == 'Redis'


def test_custom_provider(app):
    """Test that FlaskRedis can be instructed to use a different Redis client,
    like StrictRedis"""
    class FakeProvider(object):

        @classmethod
        def from_url(cls, *args, **kwargs):
            return cls()

    redis = FlaskRedis.from_custom_provider(FakeProvider)
    assert redis._redis_client is None
    redis.init_app(app)
    assert redis._redis_client is not None
    assert isinstance(redis._redis_client, FakeProvider)
