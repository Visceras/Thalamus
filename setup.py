#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of thalamus.
# https://github.com/Visceras/Thalamus

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2015, Francisco J. Piedrahita <franciscojpiedrahita@gmail.com>

from setuptools import setup, find_packages
from thalamus import __version__

tests_require = [
    'mock',
    'nose',
    'coverage',
    'yanc',
    'preggy',
    'tox',
    'ipdb',
    'coveralls',
    'sphinx',
]

setup(

    # Project information
    license = 'MIT',
    name = 'thalamus',
    version = __version__,
    url = 'https://github.com/Visceras/Thalamus',
    description = 'MQTT Broker written in Python',
    long_description = '''MQTT Broker written in Python''',

    keywords = 'MQTT 3.1.1 broker IOT Queue Telemetry OASIS',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 2.7',
        'Operating System :: OS Independent',
    ],


    # Author information
    author = 'Francisco J. Piedrahita',
    author_email = 'franciscojpiedrahita@gmail.com',


    # Project configuration
    packages=find_packages(),
    include_package_data=True,

    install_requires=[
        # add your dependencies here
        # remember to use 'package-name>=x.y.z,<x.y+1.0' notation (this way you get bugfixes)
    ],

    extras_require={
        'tests': tests_require,
    },

    entry_points={
        'console_scripts': [
            # add cli scripts here in this form:
            # 'thalamus=thalamus.cli:main',
        ],
    },
)
