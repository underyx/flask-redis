#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()


setup(
    name='Flask-Redis',
    version='0.0.6',
    url='http://github.com/rhyselsmore/flask-redis',
    author='Rhys Elsmore',
    author_email='me@rhys.io',
    description='Redis Extension for Flask Applications',
    long_description=open('README.rst').read() + '\n\n' +
        open('HISTORY.rst').read(),
    py_modules=['flask_redis'],
    license=open('LICENSE').read(),
    package_data={'': ['LICENSE']},
    zip_safe=False,
    platforms='any',
    install_requires=[
        'setuptools',
        'Flask>=0.8',
        'Redis>=2.7.6'
    ],
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
