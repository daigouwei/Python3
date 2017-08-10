#!/usr/bin/env
#-*- coding:utf-8 -*-

CARF_ENABLED = True      #激活跨站点请求伪造保护
SECRET_KEY = 'python99'  #加密令牌用于验证一个表单
SQLALCHEMY_TRACK_MODIFICATIONS = False    #消除一个警告

#为sqlite服务
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')   #Flask-SQLAlchemy 扩展需要的，该变量存储我们数据库文件的路径。
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')           #文件夹将会把 SQLAlchemy-migrate 数据文件存储在这里。
