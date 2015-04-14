History
=======

0.1.0 (4/15/2015)
-----------------

- **Deprecation:** Renamed ``flask_redis.Redis`` to ``flask_redis.FlaskRedis``.
  Using the old name still works, but emits a deprecation warning, as it will
  be removed from the next version
- **Deprecation:** Setting a ``REDIS_DATABASE`` (or equivalent) now emits a
  depracation warning as it will be removed in the version in favor of
  including the database number in ``REDIS_URL`` (or equivalent)
- Added a ``FlaskRedis.from_custom_provider(provider)`` class method for using
  any redis provider class that supports instantiation with a ``from_url``
  class method
- Added a ``strict`` parameter to ``FlaskRedis`` which expects a boolean value
  and allows choosing between using ``redis.StrictRedis`` and ``redis.Redis``
  as the defualt provider.
- Made ``FlaskRedis`` register as a Flask extension through Flask's extension
  API
- Rewrote test suite in py.test
- Got rid of the hacky attribute copying mechanism in favor of using the
  ``__getattr__`` magic method to pass calls to the underlying client

0.0.6 (4/9/2014)
----------------

- Improved Python 3 Support (Thanks underyx!).
- Improved test cases.
- Improved configuration.
- Fixed up documentation.
- Removed un-used imports (Thanks underyx and lyschoening!).


0.0.5 (17/2/2014)
----------------

- Improved support for the config prefix.

0.0.4 (17/2/2014)
----------------

- Added support for config_prefix, allowing multiple DBs.

0.0.3 (6/7/2013)
----------------

- Added TravisCI Testing for Flask 0.9/0.10.
- Added Badges to README.

0.0.2 (6/7/2013)
----------------

- Implemented a very simple test.
- Fixed some documentation issues.
- Included requirements.txt for testing.
- Included task file including some basic methods for tests.

0.0.1 (5/7/2013)
----------------

- Conception
- Initial Commit of Package to GitHub.
