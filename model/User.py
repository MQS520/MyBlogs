#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: MQS
# datetime:2018/12/29 15:11
# software: PyCharm
# desc:
from app import db
import json

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(120),index=True,unique=True)
    password = db.Column(db.String(128))
    createtime = db.Column(db.TIMESTAMP)

    def __init__(self, username, email, password):
        self.username = username
        self.password = password
        self.email = email


# class Result:
#
#     def __init__(self, status, msg):
#         self.status = status
#         self.msg = msg
#
#     def __str__(self):
#         return "status:[%s],msg:[%s]" % (self.status, self.msg)

def result(status, msg):
    result = {
        'status': status,
        'msg': msg
    }
    return result

