# flask-redis

[![CircleCI](https://circleci.com/gh/underyx/flask-redis.svg?style=svg)](https://circleci.com/gh/underyx/flask-redis)
[![codecov](https://codecov.io/gh/underyx/flask-redis/branch/master/graph/badge.svg)](https://codecov.io/gh/underyx/flask-redis)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/8f8297c1a5f542d49429c4837165984f)](https://www.codacy.com/app/bence/flask-redis?utm_source=github.com&utm_medium=referral&utm_content=underyx/flask-redis&utm_campaign=Badge_Grade)
[![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/underyx/flask-redis.svg)](https://github.com/underyx/flask-redis/tags)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flask-redis.svg)
![Flask version support is 0.9+](https://img.shields.io/badge/flask-0.9%2B-blue.svg)
![redis-py version support is 2.6+](https://img.shields.io/badge/redis--py-2.6%2B-blue.svg)
[![Code style: black](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/ambv/black)

A nice way to use Redis in your Flask app.

## Configuration

Start by installing the extension with `pip install flask-redis`.
Once that's done, configure it within your Flask config.
Set the URL of your Redis instance like this:

```python
REDIS_URL = "redis://:password@localhost:6379/0"
```

If you wanna connect to a Unix socket,
you can specify it like `"unix://:password@/path/to/socket.sock?db=0"`.

## Usage

### Setup

To add a Redis client to your application:

```python
from flask import Flask
from flask_redis import FlaskRedis

app = Flask(__name__)
redis_client = FlaskRedis(app)
```

or if you prefer, you can do it the other way around:

```python
redis_client = FlaskRedis()
def create_app():
    app = Flask(__name__)
    redis_client.init_app(app)
    return app
```

The `FlaskRedis` client here will pass its keyword arguments
to the [`Redis` class](https://redis-py.readthedocs.io/en/latest/#redis.Redis)
from the [`redis-py`](https://github.com/andymccurdy/redis-py) library,
so all parameters from the `Redis` documentation page will work here as well
— such as `socket_timeout` and `encoding`.

### Accessing Redis

Access is done by using `FlaskRedis` as if it was a
[`Redis` class](https://redis-py.readthedocs.io/en/latest/#redis.Redis)
as well:

```python
from my_app import redis_client

@app.route('/')
def index():
    return redis_client.get('potato')
```

For detailed instructions on what methods you can use on the client,
as well as how you can use advanced features
such as Lua scripting, pipelines, and callbacks,
please check the
[redis-py documentation](https://redis-py.readthedocs.io/en/latest/).

**Pro-tip:** The [redis-py](https://github.com/andymccurdy/redis-py)
package uses the `redis` namespace, so it's nicer to name your Redis object something like `redis_client` instead of just `redis`.

## Extra features in flask-redis

### Custom providers

Instead of the default `Redis` client from `redis-py`,
you can provide your own.
This can be useful to replace it with [mockredis](https://github.com/locationlabs/mockredis) for testing:

```python
from flask import Flask
from flask_redis import FlaskRedis
from mockredis import MockRedis


def create_app():
    app = Flask(__name__)
    if app.testing:
        redis_store = FlaskRedis.from_custom_provider(MockRedis)
    else:
        redis_store = FlaskRedis()
    redis_store.init_app(app)
    return app
```

## Contributing

1. Check for open issues or open a fresh issue to start a discussion
2. Fork [the repository](https://github.com/underyx/flask-redis) on GitHub.
3. Send a pull request with your code!

Merging will require a test which shows that the bug was fixed,
or that the feature works as expected.
Feel free to open a draft pull request though without such a test
and ask for help with writing it if you're not sure how to.

As [Bence](https://underyx.me) (the only maintainer) works full-time,
please allow some time before your issue or pull request is handled.
