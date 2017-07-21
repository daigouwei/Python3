#!/usr/bin/env
#-*- coding:utf-8 -*-

from flask import Flask

app = Flask('app')
app.config.from_object('config')

from app import views
