#!/usr/bin/env
#-*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object('config')   #读取配置文件config

db = SQLAlchemy(app)      #实例化数据库ORM

lm = LoginManager()    #初始化flask-login
lm.setup_app(app)

from app import views, models
