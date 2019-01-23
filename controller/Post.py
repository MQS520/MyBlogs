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

import time
import json
import base64
import hashlib
import requests

# 发布贴子
class Add(Resource):
    def post(self):
        post = request.json
        token = post['token']
        id = verify_token(token)
        if id == 0:
            return Result(False, '登录信息失效，请重新登录！', None)
        title = post['title']
        content = post['centent']
        db.session.add(Post(id, title, content))
        db.session.commit()
        return Result(True, '发布成功!', None)

