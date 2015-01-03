#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Flask-Redis."""

import flask
from flask_redis import Redis
import redis
import unittest


class FlaskRedisTestCase(unittest.TestCase):

    def setUp(self):
        """ Create a sample Flask Application """
        self.redis = Redis()
        self.app = flask.Flask(__name__)

    def test_init_app(self):
        """ Test the initation of our Redis extension """
        self.redis.init_app(self.app)
        assert self.redis.get('potato') is None

    def test_custom_prefix(self):
        """ Test the use of custom config prefixes """
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

    def test_strict_redis(self):
        r = Redis(config_prefix='TEST_STRICT')
        self.app.config['TEST_STRICT_CLASS'] = redis.StrictRedis
        r.init_app(self.app)
        assert r._redisclass == redis.client.StrictRedis

    def test_nonstrict_redis(self):
        r = Redis(config_prefix='TEST_NON_STRICT')
        r.init_app(self.app)
        assert r._redisclass == redis.client.Redis
