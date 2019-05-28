import codecs
import os
import re

from setuptools import find_packages, setup


NAME = "flask-redis"
KEYWORDS = ["flask", "redis"]
CLASSIFIERS = [
    "Development Status :: 4 - Beta",
    "Environment :: Web Environment",
    "Framework :: Flask",
    "Intended Audience :: Developers",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: Implementation :: CPython",
    "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    "Topic :: Software Development :: Libraries :: Python Modules",
]


PROJECT_URLS = {
    "Bug Tracker": "https://github.com/underyx/flask-redis/issues",
    "Source Code": "https://github.com/underyx/flask-redis",
}

INSTALL_REQUIRES = ["Flask>=0.8", "redis>=2.7.6"]
EXTRAS_REQUIRE = {"tests": ["coverage", "pytest", "pytest-mock"]}
EXTRAS_REQUIRE["dev"] = EXTRAS_REQUIRE["tests"] + ["pre-commit"]


def read(*parts):
    """
    Build an absolute path from *parts* and return the contents of the resulting file.

    Assumes UTF-8 encoding.
    """
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, *parts), "rb", "utf-8") as f:
        return f.read()


META_FILE = read("flask_redis", "__init__.py")


def find_meta(meta):
    """Extract __*meta*__ from META_FILE."""
    meta_match = re.search(
        r"^__{meta}__ = ['\"]([^'\"]*)['\"]".format(meta=meta), META_FILE, re.M
    )
    if meta_match:
        return meta_match.group(1)
    raise RuntimeError("Unable to find __{meta}__ string.".format(meta=meta))


setup(
    name=find_meta("title"),
    description=find_meta("description"),
    version=find_meta("version"),
    url=find_meta("url"),
    author=find_meta("author"),
    author_email=find_meta("email"),
    maintainer=find_meta("author"),
    maintainer_email=find_meta("email"),
    download_url=find_meta("url") + "releases",
    keywords=KEYWORDS,
    long_description=(
        read("README.md")
        + "\n\n"
        + re.sub("^#", "##", read("CHANGELOG.md"))
        + "\n\n"
        + re.sub("^#", "##", read("AUTHORS.md"))
    ),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=CLASSIFIERS,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    include_package_data=True,
)
