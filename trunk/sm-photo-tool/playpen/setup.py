#!/usr/bin/python

from distutils.core import setup

setup(name="zmugjson",
      version="0.1",
      description="zmugjson a smugmug.com JSON api",
      long_description="A JSON-based api wrapper used to connect to smugmug.com",
      author="Jesus M. Rodriguez",
      author_email="jmrodri@nc.rr.com",
      url="http://zmugtools.sourceforge.net",
      py_modules=["zmugjson", "config"],
      license="GPL",
      data_files = [("/etc/zmugjson", ["logger.conf"])
      ]
     )
