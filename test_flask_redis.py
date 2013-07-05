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
        self.app = flask.Flask('test-flask-redis')

    def test_init_app(self):
        """ Test the initation of our Redis extension """
        self.redis.init_app(self.app)
        assert self.redis.get('test') is None
