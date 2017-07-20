#!/usr/bin/env
#-*- coding:utf-8 -*-

from flask import Flask
app = Flask('app')
from app import views
