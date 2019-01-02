#!/usr/bin/env python
# encoding: utf-8
'''
@author: MQS
@file: common.py
@time: 2019-01-02 21:55
@desc:
'''
from flask import session
from utils import KeyUtil


# 返回结果
def Result(status, msg, data):
    result = {
        'status': status,
        'msg': msg,
        'data': data
    }
    return result

# 验证token, 获取user_id
def verify_token(token):
    user_id = session.get(token)
    if user_id == None:
        return 0
    bool = KeyUtil.verify_token(user_id, token)
    if bool:
        return user_id
    else:
        return 0