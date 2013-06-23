from setuptools import setup


setup(
    name='Flask-Redis',
    version='0.1',
    url='http://github.com/rhyselsmore/flask-redis',
    license='Apache2',
    author='Rhys Elsmore',
    author_email='me@rhys.io',
    description='Adds Redis support to your Flask application',
    long_description=__doc__,
    py_modules=['flask_redis'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'setuptools',
        'Flask',
        'Redis'
    ],
    test_suite='test_flask.suite',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)