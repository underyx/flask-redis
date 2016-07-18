from invoke import task


@task
def test(ctx):
    ctx.run('/usr/bin/env py.test test_flask_redis.py', pty=True)


@task
def coverage(ctx):
    ctx.run('/usr/bin/env py.test --cov-report term-missing --cov=flask_redis', pty=True)


@task
def pep8(ctx):
    ctx.run('/usr/bin/env py.test --pep8 flask_redis.py test_flask_redis.py -m pep8', pty=True)


@task
def full(ctx):
    ctx.run('/usr/bin/env py.test --pep8 --cov=flask_redis flask_redis.py test_flask_redis.py', pty=True)


@task
def travisci(ctx):
    ctx.run('/usr/bin/env py.test --pep8 --cov=flask_redis flask_redis.py test_flask_redis.py')
