#!/usr/bin/env
#-*- coding:utf-8 -*-

from flask_wtf import FlaskForm
from wtforms import TextField, BooleanField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import Required, Email, Length

class LoginForm(FlaskForm):
    # name = TextField('Name', validators=[Required()])
    # password = PasswordField('password', validators=[Required()])
    # remember_me = BooleanField('Remember_me', default=False)
    user_name = TextField('user name', validators = [Required(), Length(max = 15)])
    remember_me = BooleanField('remember me', default = False)
    submit = SubmitField('Log in')

class SignUpForm(FlaskForm):
    user_name = TextField('user name', validators = [Required(), Length(max = 15)])
    user_email = TextField('user email', validators = [Email(), Required(), Length(max = 128)])
    submit = SubmitField('Sign up')
