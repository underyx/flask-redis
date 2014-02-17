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

    def _convert(self, arg, val):
        """
        Apply a conversion method to specific arguments i.e. ports
        """
        return self.converters[arg](val) if arg in self.converters else val

    def _get_connection_class_args(self, c):
        """
        Returns the args that are expected by the Redis class
        """
        return ([a.upper() for a in inspect.getargspec(c.__init__).args
                if a != 'self'])

    def _parse_configuration(self, url=None):
        """
        Parse the configuration attached to our application. We provide
        URL as a default, and other set values (including URL) will override
        the defaults that are parsed.
        """
        if url:
            urlparse.uses_netloc.append('redis')
            url = urlparse.urlparse(url)

            self.app.config[self.key('HOST')] = url.hostname
            self.app.config[self.key('PORT')] = url.port or 6379
            self.app.config[self.key('USER')] = url.username
            self.app.config[self.key('PASSWORD')] = url.password
            db = url.path.replace('/', '')
            self.app.config[self.key('DB')] = db if db.isdigit() else 0

        host = self.app.config.get(self.key('HOST'), '')

        if host.startswith('file://') or host.startswith('/'):
            self.app.config.pop(key('HOST'))
            self.app.config[key('UNIX_SOCKET_PATH')] = host

    def _generate_connection_kwargs(self, args):
        """
        Generates the kwargs for the Redis class
        """

        def value(arg):
            """
            Returns the value of the argument from the application config
            """
            return self._convert(arg, self.app.config[self.key(arg)])

        args = [arg for arg in args if self.key(arg) in self.app.config]
        return dict([(arg.lower(), value(arg)) for arg in args])

    def init_app(self, app):
        """
        Apply the Flask app configuration to a Redis object
        """
        self.app = app

        if self.config_prefix:
            self.key = lambda suffix: '{0}_REDIS_{1}'.format(
                self.config_prefix,
                suffix
            )
        else:
            self.key = lambda suffix: 'REDIS_{0}'.format(suffix)

        self.app.config.setdefault(self.key('URL'), 'redis://localhost/0')

        klass = app.config.get(self.key('CLASS'), RedisClass)

        if isinstance(klass, basestring):
            klass = import_string(klass)

        self._parse_configuration(self.app.config.get(self.key('URL')))
        args = self._get_connection_class_args(klass)
        kwargs = self._generate_connection_kwargs(args)
        self.connection = connection = klass(**kwargs)
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
