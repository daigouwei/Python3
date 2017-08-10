#!/usr/bin/env
#-*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')   #读取配置文件config
db = SQLAlchemy(app)      #实例化数据库ORM

from app import views, models
