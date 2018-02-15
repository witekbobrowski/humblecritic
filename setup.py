# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='humble-rating',
    version='0.1.0',
    description=' Goodreads rates for books from HumbleBundle book bundles',
    long_description=readme,
    author='Witek Bobrowski',
    author_email='witek@bobrowski.com.pl',
    url='https://github.com/witekbobrowski/humble-rating',
    license=license,
    packages=find_packages(exclude=('tests'))
)
