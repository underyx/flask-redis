Flask-Redis
===========

Add Redis Support to Flask.

Built on top of redis-py

Currently a single namespace within the configuration is supported.

.. code-block:: pycon

    REDIS_URL="redis://localhost"

with the Redis instance automatically loading variables from this namespace.

In the future, the ability to declare multiple Redis namespaces will be available

.. code-block:: pycon

    REDIS_CACHE_URL="redis://localhost/0"
    REDIS_METRICS_URL="redis://localhost/0"

    redis_cache = Redis(config_prefix="REDIS_CACHE")
    redis_metrics = Redis(config_prefix="REDIS_METRICS")

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

**ToDo** Add Settings

.. code-block:: pycon

    from flask import Flask
    from flask_redis import Redis

    app = Flask(__name__)
    redis_store = Redis(app)

or

.. code-block:: pycon

    from flask import Flask
    from flask_redis import Redis

    redis_store = Redis()

    def create_app():
        app = Flask(__name__)
        redis.init_app(app)
        return app

Usage
-----

.. code-block:: pycon

    from core import redis_store

    @app.route('/')
    def index():
        return redis_store.get('potato','Not Set')

`redis-py <https://github.com/andymccurdy/redis-py>`_

**Protip:** The `redis-py <https://github.com/andymccurdy/redis-py>`_ package currently holds the 'redis' namespace,
so if you are looking to make use of it, your Redis object shouldn't be named 'redis'.

For detailed instructions regarding the usage of the client, check the `redis-py <https://github.com/andymccurdy/redis-py>`_ documentation.

Advanced features, such as Lua scripting, pipelines and callbacks are detailed within the projects README.
