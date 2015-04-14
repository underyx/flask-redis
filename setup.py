#!/usr/bin/env python3

import io
from setuptools import setup


with io.open('README.rst', encoding='utf-8') as f:
    readme = f.read()
with io.open('HISTORY.rst', encoding='utf-8') as f:
    history = f.read()
with io.open('LICENSE', encoding='utf-8') as f:
    license = f.read()


setup(
    name='Flask-Redis',
    version='0.1.0',
    url='https://github.com/underyx/flask-redis',
    author='Rhys Elsmore',
    author_email='me@rhys.io',
    maintainer='Bence Nagy',
    maintainer_email='bence@underyx.me',
    download_url='https://github.com/underyx/flask-redis/releases',
    description='Redis Extension for Flask Applications',
    long_description=readme + '\n\n' + history,
    py_modules=['flask_redis'],
    license=license,
    package_data={'': ['LICENSE']},
    zip_safe=False,
    install_requires=[
        'Flask>=0.8',
        'redis>=2.7.6',
    ],
    extras_require={
        'develop': [
            'invoke',
        ],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Flask',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
