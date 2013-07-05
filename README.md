Flask-Redis
===========

Add Redis Support to Flask.

Built on top of redis-py

Currently a single namespace within the configuration is supported. 

```
REDIS_URL="redis://localhost"
```

with the Redis instance automatically loading variables from this namespace.

In the future, the ability to declare multiple Redis namespaces will be available

```
REDIS_CACHE_URL="redis://localhost/0"
REDIS_METRICS_URL="redis://localhost/0"

redis_cache = Redis(config_prefix="REDIS_CACHE")
redis_metrics = Redis(config_prefix="REDIS_METRICS")
```

## Installation 

```
pip install flask-redis
```

Or if you *must* use easy_install:

```
alias easy_install="pip install $1"
easy_install flask-redis
```

## Configuration

**ToDo** Add Settings

```
from flask import Flask
from flask_redis import Redis

app = Flask(__name__)
redis_store = Redis(app)
```

or

```
from flask import Flask
from flask_redis import Redis

redis_store = Redis()

def create_app():
    app = Flask(__name__)
    redis.init_app(app)
    return app
```

## Usage

```
from core import redis_store

@app.route('/')
def index():
    return redis_store.get('potato','Not Set')
```

**Protip:** The [redis-py](https://github.com/andymccurdy/redis-py) package currently holds the 'redis' namespace, 
so if you are looking to make use of it, your Redis object shouldn't be named 'redis'.

For detailed instructions regarding the usage of the client, check the [redis-py](https://github.com/andymccurdy/redis-py) documentation.

Advanced features, such as Lua scripting, pipelines and callbacks are detailed within the projects README. 
