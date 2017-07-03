#!/usr/bin/env
#-*- coding:utf-8 -*-

from setuptools import setup

setup(
    name='oa',
    py_modules=['oa'],
    install_requires=['bs4', 'selenium'],
    entry_points={
        'console_scripts': ['oa=oa:commandLineInterface']
    }
)
