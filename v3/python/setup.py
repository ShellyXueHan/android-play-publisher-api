#!/usr/bin/env python
# -*- encoding: utf-8 -*-


'''
take the structure from airwatch cli tool:
(ref: https://github.com/benedicteb/pyAirWatch)

'''


import sys
import re
import os.path as op

from setuptools import setup

def get_version():
    contents = ''

    with open(op.join('googleDeploymentAPI', '__init__.py'), 'r') as infile:
        contents = infile.read()

    try:
        version = re.search(r"__version__ = '(.+)'", contents).group(1)
    except Exception as e:
        raise Exception('Unable to find version. Files may be damaged.')

    return version

name='pyGoogleDeploymentAPI'
version=get_version()
description='CLI tool to call Google Android Deployment API.'

author='Shelly Han'
author_email='shell@freshworks.io'

packages=['googleDeploymentAPI']

install_requires=[
    'google-api-python-client',
]

setup(name=name,
      version=version,
      description=description,
      author=author,
      author_email=author_email,
      packages=packages,
      install_requires=install_requires)
