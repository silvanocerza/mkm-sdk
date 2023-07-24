# -*- coding: utf-8 -*-
# !/usr/bin/env python

from setuptools import setup, find_packages
import sys
import os
import re


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    """
    init_py = open(os.path.join(package, "__init__.py")).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version("mkmsdk")


LONG_DESCRIPTION = open("README.md").read()


if sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    print("You probably want to also tag the version now:")
    print(" git tag -a %s -m '%s'" % (version, version))
    print(" git push --tags")
    sys.exit()

keywords = " ".join(
    [
        "mkm",
        "magickardmarket",
        "magiccardmarket",
        "sdk",
        "mtg",
        "magic the gathering",
        "card",
        "market",
        "rest",
        "tcg",
        "trading card game",
        "pokemon",
        "wow",
        "world of warcraft",
        "yugioh",
    ]
)

setup(
    name="mkmsdk",
    version=version,
    author="Silvano Cerza",
    packages=find_packages(exclude=["docs", "tests*"]),
    scripts=[],
    url="https://github.com/silvanocerza/mkm-sdk",
    license="MIT",
    description="MagicKardMarket sdk",
    long_description=LONG_DESCRIPTION,
    install_requires=["requests", "requests_oauthlib"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=keywords,
)
