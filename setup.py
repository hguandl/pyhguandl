#!/usr/bin/env python3

from distutils.core import setup

setup(name='hguandl',
      version='2018.12.04',
      description='Python port for libhguandl',
      python_requires='>3.0',
      url='https://github.com/hguandl/pyhguandl',
      author='hguandl',
      packages=['hguandl', 'hguandl.lib', 'hguandl.samples'],
      package_data = {
        '': ['README.md']
      }
     )
