#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author: MQS
# datetime:2018/12/29 15:21
# software: PyCharm
# desc:
import time
import base64
import hmac
import hashlib

# 密码加密
def generate_password(password):
    str = password + "salt"
    new_pwd = hashlib.md5(str.encode('utf-8')).hexdigest()
    return new_pwd

# 生成 token
def generate_token(key, expire = 3600):
    # 设置token 有效期 3600s
    ts_str = str(time.time() + 3600)
    ts_type = ts_str.encode('utf-8')
    sha1_tshexstr = hmac.new(str(key).encode('utf-8'), ts_type, 'sha1').hexdigest()
    token = ts_str + ':' + sha1_tshexstr
    b64_token = base64.urlsafe_b64encode(token.encode('utf-8'))
    return b64_token.decode('utf-8')


# 验证 token
def verify_token(key, token):
    token_str = base64.urlsafe_b64decode(token).decode('utf-8')
    token_list = token_str.split(':')
    if len(token_list) != 2:
        return False
    ts_str = token_list[0]
    if float(ts_str) < time.time():
        # token 过期
        return False
    known_sha1_tsstr = token_list[1]
    calc_sha1_tsstr = hmac.new(key.encode('utf-8'), ts_str, 'sha1').hexdigest()
    if calc_sha1_tsstr != known_sha1_tsstr:
        return False
    return True