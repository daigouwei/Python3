#!/usr/bin/python3.5
#-*- coding:utf-8 -*-

from flask import render_template, flash, redirect
from app.forms import LoginForm
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = { 'nickname': 'Miguel' }
    posts = [
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
                           title = 'Home',
                           user = user,
                           posts = posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for Name: ' + form.name.data)
        flash('passwd: ' + str(form.password.data))
        flash('remember_me: ' + str(form.remember_me.data))
        return redirect('/index')           #告诉网页浏览器引导到一个不同的页面而不是请求的页面。
    return render_template('login.html',
                           title = 'Sign In',
                           form = form)
