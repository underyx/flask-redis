from redis import Redis as RedisClass

__all__ = ('Redis',)


class Redis(object):

    def __init__(self, app=None, config_prefix=None):
        """
        Constructor for non-factory Flask applications
        """

        self.config_prefix = config_prefix or 'REDIS'

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        Apply the Flask app configuration to a Redis object
        """
        self.app = app

        self.key = lambda suffix: '{0}_{1}'.format(
            self.config_prefix,
            suffix
        )

        self.app.config.setdefault(self.key('URL'), 'redis://localhost:6379')

        db = self.app.config.get(self.key('DATABASE'))

        self.connection = connection = RedisClass.from_url(
            self.app.config.get(self.key('URL')),
            db=db,
        )

        self._include_connection_methods(connection)

    def _include_connection_methods(self, connection):
        """
        Include methods from connection instance to current instance.
        """
        for attr in dir(connection):
            value = getattr(connection, attr)
            if attr.startswith('_') or not callable(value):
                continue
            self.__dict__[attr] = value
