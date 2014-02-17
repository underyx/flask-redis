#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for Flask-Redis."""

import flask
from flask_redis import Redis
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
        self.redis = Redis(config_prefix='MOOP')
        self.redis.init_app(self.app)
        assert self.app.config.get('MOOP_REDIS_URL') is not None
        assert self.redis.get('potato') is None
