Flask-Redis
===========

Adds Redis Support to Flask. Dead Simple.

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

app = Flask(__name__)
redis = Redis()
redis.init_app(app)
```
