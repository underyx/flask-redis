#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Flask-Redis."""

import flask
from flask_redis import Redis
import unittest
from mock import patch
from mockredis import mock_redis_client


class FlaskRedisTestCase(unittest.TestCase):

    def setUp(self):
        """ Create a sample Flask Application """
        self.redis = Redis()
        self.app = flask.Flask(__name__)

    @patch('redis.Redis.from_url')
    def test_init_app(self, redis_from_url):
        """ Test the initation of our Redis extension """
        redis_from_url.return_value = mock_redis_client()

        self.redis.init_app(self.app)
        assert self.redis.get('potato') is None
        assert hasattr(self.app, 'extensions')
        assert 'redis' in self.app.extensions
        assert self.redis == self.app.extensions['redis']

    @patch('redis.Redis.from_url')
    def test_custom_prefix(self, redis_from_url):
        """ Test the use of custom config prefixes """

        redis_from_url.return_value = mock_redis_client()

        self.db1_redis = Redis(config_prefix='DB1')
        self.app.config['DB1_URL'] = "redis://localhost:6379"
        self.app.config['DB1_DATABASE'] = 0
        self.db1_redis.init_app(self.app)

        self.db2_redis = Redis(config_prefix='DB2')
        self.app.config['DB2_URL'] = "redis://localhost:6379"
        self.app.config['DB2_DATABASE'] = 1
        self.db2_redis.init_app(self.app)

        self.db3_redis = Redis(config_prefix='DB3')
        self.app.config['DB3_URL'] = "redis://localhost:6379"
        self.db3_redis.init_app(self.app)

        self.db4_redis = Redis(config_prefix='DB4')
        self.app.config['DB4_URL'] = "redis://localhost:6379/5"
        self.db4_redis.init_app(self.app)

        assert self.db1_redis.get('potato') is None
        assert self.db2_redis.get('potato') is None
        assert self.db3_redis.get('potato') is None
        assert self.db4_redis.get('potato') is None
