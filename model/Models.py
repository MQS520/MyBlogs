#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: MQS
# datetime:2018/12/29 15:11
# software: PyCharm
# desc:
from app import db
import datetime

# user表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    account = db.Column(db.String(64))
    username = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(120),index=True,unique=True)
    password = db.Column(db.String(128))
    createtime = db.Column(db.DateTime, default=datetime.datetime.now)

    # 数据库中 id自增长，createtime 默认当前时间
    def __init__(self, account, username, email, password):
        self.account = account
        self.username = username
        self.password = password
        self.email = email

# 文章表
class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    title = db.Column(db.String(255))
    content = db.Column(db.Text(1000))
    comments = db.Column(db.Integer, default=0)
    like = db.Column(db.Integer, default=0)
    createtime = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, user_id, title, content):
        self.user_id = user_id
        self.title = title
        self.content = content

