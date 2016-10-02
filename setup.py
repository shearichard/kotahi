# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='kotahi',
    version='0.0.1',
    description='Board Game Strategy Testbed',
    long_description=readme,
    author='Richard Shea',
    author_email='rshea@thecubagroup.com',
    url='https://github.com/shearichard/kotahi',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

