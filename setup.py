# -*- coding: utf-8 -*-
from setuptools import find_namespace_packages
from setuptools import setup

setup(
    name='hydromel',
    version='0.0.1',
    description='Splunk app for SIGMA',
    author='ljk',
    author_email='ljk',
    entry_points={},
    install_requires=[
        'sigmatools==0.20.0',
        'ruamel.yaml==0.17.16',
        'jinja2==3.0.2'
    ],
    python_requires='>=3.6.*, <4',
)
