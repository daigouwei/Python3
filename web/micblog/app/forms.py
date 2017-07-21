#!/usr/bin/env
#-*- coding:utf-8 -*-

# from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, PasswordField
from wtforms.validators import Required

class LoginForm(FlaskForm):
    name = TextField('Name', validators=[Required()])
    password = PasswordField('password', validators=[Required()])
    remember_me = BooleanField('Remember', default=False)
