#!/usr/bin/env python
# encoding: utf-8
'''
@author: MQS
@file: route.py
@time: 2018-12-30 12:22
@desc:
'''
from app import app
from controller import User, Post
from flask_restful import Api

api = Api(app)

api.add_resource(User.Login, '/login')
api.add_resource(User.Regist, '/regist')
api.add_resource(User.Modify,'/user/modify')
api.add_resource(Post.Add, '/post/add')
