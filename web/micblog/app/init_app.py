#!/usr/bin/env
#-*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask('app')
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from app import views, models
