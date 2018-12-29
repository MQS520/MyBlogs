#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: MQS
# datetime:2018/12/29 15:11
# software: PyCharm
# desc:
from app import db

# user表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(120),index=True,unique=True)
    password = db.Column(db.String(128))
    createtime = db.Column(db.TIMESTAMP)

    # 数据库中 id自增长，createtime 默认当前时间
    def __init__(self, username, email, password):
        self.username = username
        self.password = password
        self.email = email

