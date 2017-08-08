#!/usr/bin/python3.5
#-*- coding:utf-8 -*-

from flask import Flask
app = Flask(__name__)
app.config.from_object('config')   #读取配置文件config

from app import views
