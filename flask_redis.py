from redis import Redis as RedisClass
import inspect
import urlparse
from werkzeug.utils import import_string

__all__ = ('Redis',)


class Redis(object):

    converters = {'port': int}

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

        self.app.config.setdefault(self.key('URL'), 'redis://localhost')
        self.app.config.setdefault(self.key('DATABASE'), 0)

        db = self.app.config.get(self.key('DATABASE'))


        if not str(db).isdigit() or not isinstance(db, int):
            raise ValueError('A valid DB must be supplied')

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
