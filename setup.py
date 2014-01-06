#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: sw=4 ts=4 fenc=utf-8 ft=python cc=100 tw=99 et
'''
    setup.py
    ~~~~~~~~

    Package Setup

    :codeauthor: :email:`Pedro Algarvio (pedro@algarvio.me)`
    :copyright: © 2013 by the SaltStack Team, see AUTHORS for more details.
    :license: Apache 2.0, see LICENSE for more details.
'''

import os
import subprocess
from setuptools import setup
from distutils import log
from distutils.command import clean, build
from distutils.extension import Extension

import pylinthelpers as package


setup(name=package.__package_name__,
      version=package.__version__,
      author=package.__author__,
      author_email=package.__email__,
      url=package.__url__,
      description=package.__summary__,
      long_description=package.__description__,
      license=package.__license__,
      keywords=package.__keywords__,
      packages=[
          'pylinthelpers',
          'pylinthelpers.brain'
      ],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: Apache 2.0 License',
          'Programming Language :: Python',
          'Topic :: Utilities',
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Topic :: Software Development :: Quality Assurance",
      ]
)
