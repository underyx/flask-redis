Flask-Redis
===========

.. image:: https://api.travis-ci.org/underyx/flask-redis.svg?branch=master
   :target: https://travis-ci.org/underyx/flask-redis
   :alt: Build Status

.. image:: https://codecov.io/gh/underyx/flask-redis/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/underyx/flask-redis
   :alt: Coverage Status

.. image:: https://landscape.io/github/underyx/flask-redis/master/landscape.svg
           ?style=flat
   :target: https://landscape.io/github/underyx/flask-redis
   :alt: Code Health

Adds Redis support to Flask.

Built on top of redis-py_.

Contributors
------------

- Rhys Elsmore - @rhyselsmore - https://github.com/rhyselsmore
- Bence Nagy - @underyx - https://github.com/underyx
- Lars Schöning - @lyschoening - https://github.com/lyschoening
- Aaron Tygart - @thekuffs - https://github.com/thekuffs
- Christian Sueiras - @csueiras - https://github.com/csueiras


Installation
------------

.. code-block:: bash

    pip install flask-redis

Or if you *must* use easy_install:

.. code-block:: bash

    alias easy_install="pip install $1"
    easy_install flask-redis


Configuration
-------------

Your configuration should be declared within your Flask config. Set the URL of
your database like this:

.. code-block:: python

    REDIS_URL = "redis://:password@localhost:6379/0"
    # or
    REDIS_URL = "unix://[:password]@/path/to/socket.sock?db=0"


To create the redis instance within your application

.. code-block:: python

    from flask import Flask
    from flask_redis import FlaskRedis

    app = Flask(__name__)
    redis_store = FlaskRedis(app)

or

.. code-block:: python

    from flask import Flask
    from flask_redis import FlaskRedis

    redis_store = FlaskRedis()

    def create_app():
        app = Flask(__name__)
        redis_store.init_app(app)
        return app

or perhaps you want to use the old, plain ``Redis`` class instead of
``StrictRedis``

.. code-block:: python

    from flask import Flask
    from flask_redis import FlaskRedis
    from redis import StrictRedis

    app = Flask(__name__)
    redis_store = FlaskRedis(app, strict=False)

or maybe you want to use
`mockredis <https://github.com/locationlabs/mockredis>`_ to make your unit
tests simpler.  As of ``mockredis`` 2.9.0.10, it does not have the
``from_url()`` classmethod that ``FlaskRedis`` depends on, so we wrap it and add
our own.

.. code-block:: python


    from flask import Flask
    from flask_redis import FlaskRedis
    from mockredis import MockRedis



    class MockRedisWrapper(MockRedis):
        '''A wrapper to add the `from_url` classmethod'''
        @classmethod
        def from_url(cls, *args, **kwargs):
            return cls()

    def create_app():
        app = Flask(__name__)
        if app.testing:
            redis_store = FlaskRedis.from_custom_provider(MockRedisWrapper)
        else:
            redis_store = FlaskRedis()
        redis_store.init_app(app)
        return app

Usage
-----

``FlaskRedis`` proxies attribute access to an underlying Redis connection. So
treat it as if it were a regular ``Redis``
instance.

.. code-block:: python

    from core import redis_store

    @app.route('/')
    def index():
        return redis_store.get('potato', 'Not Set')

**Protip:** The redis-py_ package currently holds the 'redis' namespace, so if
you are looking to make use of it, your Redis object shouldn't be named 'redis'.

For detailed instructions regarding the usage of the client, check the redis-py_
documentation.

Advanced features, such as Lua scripting, pipelines and callbacks are detailed
within the redis-py_ README.

Contribute
----------

#. Check for open issues or open a fresh issue to start a discussion around a
   feature idea or a bug. There is a Contributor Friendly tag for issues that
   should be ideal for people who are not very familiar with the codebase yet.
#. Fork `the repository`_ on Github to start making your changes to the
   **master** branch (or branch off of it).
#. Write a test which shows that the bug was fixed or that the feature works as
   expected.
#. Send a pull request and bug the maintainer until it gets merged and
   published.

.. _`the repository`: https://github.com/underyx/flask-redis
.. _redis-py: https://github.com/andymccurdy/redis-py
