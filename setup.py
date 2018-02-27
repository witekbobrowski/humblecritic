#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# Author: Witek Bobrowski

import os
from setuptools import setup, find_packages
from humblecritic import __version__

basename = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(basename, 'README.md')) as f:
    readme = f.read()

with open(os.path.join(basename, 'LICENSE')) as f:
    license_file = f.read()

setup(
    name='humblecritic',
    version=__version__,
    description='Get score for HumbleBundle bundle',
    long_description=readme,
    author='Witek Bobrowski',
    author_email='witek@bobrowski.com.pl',
    url='https://github.com/witekbobrowski/humble-rating',
    license=license_file,
    packages=find_packages(exclude=('tests')),
    entry_points={
        'console_scripts': [
            'humblecritic = humblecritic.__main__:main'
        ]
    },
)
