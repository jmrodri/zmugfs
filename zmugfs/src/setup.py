#!/usr/bin/python

from distutils.core import setup

VERSION = open("version", "r+").read().split()[0]

setup(name="zmugfs",
      version=VERSION,
      description="zmugfs FUSE-based filesystem",
      long_description="A FUSE-based filesystem used to browse your smugmug.com account",
      author="Jesus M. Rodriguez",
      author_email="jmrodri@nc.rr.com",
      url="http://zmugtools.sourceforge.net",
      py_modules=["zmugfs"],
      license="GPL",
      scripts=["zmugfs"],
      data_files=[("/usr/share/doc/zmugfs-%s" % VERSION, ["LICENSE.TXT"]),
                    ("/etc/zmugfs", ["logger.conf"])
      ]
     )
