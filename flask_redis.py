from redis import Redis as RedisClass
import inspect
import urlparse
from werkzeug.utils import import_string

__all__ = ('Redis',)

class Redis(object):

    def __init__(self, app=None, config_prefix=None):

        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        app.config.setdefault('REDIS_URL','redis://localhost/0')

        converters = {'port': int}
        convert = lambda arg, value: (converters[arg](value)
                                      if arg in converters
                                      else value)
        key = lambda suffix: 'REDIS_{0}'.format(suffix)

        klass = app.config.get(key('CLASS'), RedisClass)

        if isinstance(klass, basestring):
            klass = import_string(klass)

        url = app.config.get(key('URL'))

        if url:
            urlparse.uses_netloc.append('redis')
            url = urlparse.urlparse(url)

            app.config[key('HOST')] = url.hostname
            app.config[key('PORT')] = url.port or 6379
            app.config[key('USER')] = url.username
            app.config[key('PASSWORD')] = url.password
            db = url.path.replace('/', '')
            app.config[key('DB')] = db if db.isdigit() else 0

        host = app.config[key('HOST')]

        if host.startswith('file://') or host.startswith('/'):
            app.config.pop(key('HOST'))
            app.config[key('UNIX_SOCKET_PATH')] = host

        args = inspect.getargspec(klass.__init__).args
        args.remove('self')

        kwargs = dict([(arg, convert(arg, app.config[key(arg.upper())]))
                       for arg in args
                       if key(arg.upper()) in app.config])

        self.connection = connection = klass(**kwargs)

        self._include_public_methods(connection)

    def _include_public_methods(self, connection):
        """
        Include public methods from connection instance to current instance.
        """
        for attr in dir(connection):
            value = getattr(connection, attr)
            if attr.startswith('_') or not callable(value):
                continue
            self.__dict__[attr] = value