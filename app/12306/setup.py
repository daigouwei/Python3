#!/usr/bin/env
#-*- coding:utf-8 -*-

from setuptools import setup

setup(
    name='12306',
    py_modules=['tickets', 'stations'],
    install_requires=['requests', 'docopt', 'prettytable', 'colorama'],
    entry_points={
        'console_scripts': ['12306=tickets:commandLineInterface']
    }
)
