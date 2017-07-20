#!/usr/bin/env
#-*- coding:utf-8 -*-

from app.init_app import app

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'
