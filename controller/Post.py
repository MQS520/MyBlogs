#!/usr/bin/env python
# encoding: utf-8
'''
@author: MQS
@file: Post.py
@time: 2019-01-02 22:24
@desc:
'''
from app import db
from flask_restful import request, Resource
from model.Models import Post
from controller.common import Result, verify_token

class Add(Resource):
    def post(self):
        post = request.json
        token = post['token']
        id = verify_token(token)
        if id == 0:
            return Result(False, '登录信息失效，请重新登录！', None)
