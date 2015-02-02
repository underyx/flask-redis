from redis import Redis as _Redis

__all__ = ('FlaskRedis',)


class FlaskRedis(object):
    def __init__(self, app=None, config_prefix='REDIS', provider=None):
        self.config_prefix = config_prefix
        self.redis_client = None
        if app is not None:
            self.init_app(app, provider=provider)

    def init_app(self, app, provider=None):
        redis_url = app.config.get('{}_URL'.format(self.config_prefix),
                                   'redis://localhost:6379/0')
        if provider is None:
            provider = _Redis
        self.redis_client = provider.from_url(redis_url)

    def __getattr__(self, name):
        return getattr(self.redis_client, name)
