#!/usr/bin/env
#-*- coding:utf-8 -*-

from flask import render_template
from app.init_app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'daigouwei'}
    posts =[
    {
        'author': {'username': 'malu'},
        'body': 'I love guowei very much!'
    },
    {
        'author': {'username': 'guowei'},
        'body': 'I love malu more than malu!'
    }
    ]
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)
