#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import xerox

from setuptools import setup


def publish():
    """Publish to PyPi"""
    os.system("python setup.py sdist upload")

if sys.argv[-1] == "publish":
    publish()
    sys.exit()

setup(name='xerox',
      version='0.4.1',
      description='Simple Copy + Paste in Python.',
      long_description=open('README.rst').read(),
      author='Kenneth Reitz',
      author_email='me@kennethreitz.com',
      url='http://github.com/kennethreitz/xerox',
      packages=['xerox'],
      entry_points={
        'console_scripts': [
          'xerox = xerox:main',
        ]
      },
      license='MIT',
      classifiers=(
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: IronPython"
        )
      )
