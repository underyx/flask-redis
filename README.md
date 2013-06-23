Flask-Redis
===========

Adds Redis Support to Flask. Dead Simple.

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

app = Flask(__name__)
redis = Redis()
redis.init_app(app)
```