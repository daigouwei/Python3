#!/usr/bin/env
#-*- coding:utf-8 -*-

from flask import render_template, flash, redirect
from app.forms import LoginForm
from app.init_app import app

@app.route('/')
@app.route('/index')
def index():
    print('###[flag4]###')
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    print('###[flag1]###')
    if form.validate_on_submit():
        print('###[flag2]###')
        flash('Login requested for Name: %s' % form.name.data)
        flash('password: %s' % str(form.password.data))
        flash('remember_me: %s' % str(form.remember_me.data))
        return redirect('/index')
    print('###[flag3]###')
    return render_template('login.html',
                            title='Sign In',
                            form = form)
