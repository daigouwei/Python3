#!/usr/bin/env
#-*- coding:utf-8 -*-

import datetime
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import LoginForm
from app.models import User, Post, ROLE_USER, ROLE_ADMIN
from app import app, db, lm

@lm.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

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
    if current_user.is_authenticated:
        return redirect('/index')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.login_check(request.form.get('user_name'))
        if user:
            login_user(user)
            user.last_seen = datetime.datetime.now()

            try:
                db.session.add(user)
                db.session.commit()
            except:
                flash("The Database error!")
                return redirect('/login')
       
            flash('Your name: ' + request.form.get('user_name'))
            flash('remember me? ' + str(request.form.get('remember_me')))
            return redirect('/login')

    #form = LoginForm()
    #if form.validate_on_submit():
    #    flash('Login requested for Name: ' + form.name.data)
    #    flash('passwd: ' + str(form.password.data))
    #    flash('remember_me: ' + str(form.remember_me.data))
    #    return redirect('/index')           #告诉网页浏览器引导到一个不同的页面而不是请求的页面。
    return render_template('login.html',
                           title = 'Sign In',
                           form = form)


