# author: MQS
# datetime:2018/12/29 11:16
# software: PyCharm
# desc:
from app import app, db
from model.User import User
from flask_restful import Resource, Api, request
from utils.KeyUtil import generate_password, generate_token
from config import Result
from flask import session

api = Api(app)

# 用户登录
class Login(Resource):
    def post(self):
        user = request.json
        username = user['username']
        password = user['password']
        password = generate_password(password)
        # 根据username 查询用户是否存在
        user = User.query.filter(User.username == username).first()
        if user == None:
            return Result(False, '该用户不存在，请前往注册！', None)
        if user.password != password:
            return Result(False, '密码错误！', None)
        token = generate_token(user.id)
        # 将用户token存入session中
        session[token] = user.id
        return Result(True, '登录成功！', {'token': token})

# 用户注册
class Regist(Resource):
    def post(self):
        user = request.json
        username = user['username']
        email = user['email']
        password = user['password']

        # 根据username 查询用户是否存在
        user = User.query.filter(User.username == username).first()
        if user != None:
            return Result(False, '该用户名已注册，请使用其他用户名！', None)
        # 密码加密
        password = generate_password(password)
        # 存入数据库中
        db.session.add(User(username, email, password))
        db.session.commit()
        return Result(True, '注册成功！', None)


# 注册请求路径
api.add_resource(Login, '/login')
api.add_resource(Regist, '/regist')