Flask-Redis
===========

Adds Redis Support to Flask. Dead Simple.

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

## Usage

```
from flask import Flask
from flask_redis import Redis

app = Flask(__name__)
redis = Redis(app)
```

or

```
from flask import Flask
from flask_redis import Redis

redis = Redis()

def create_app():
    app = Flask(__name__)
    redis.init_app(app)
    return app
```
