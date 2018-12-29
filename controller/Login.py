# author: MQS
# datetime:2018/12/29 11:16
# software: PyCharm
# desc:
from app import app, db
from model import User
from flask_restful import Resource, Api, request
import json

api = Api(app)

class Login(Resource):
    def post(self):
        return {'hello':'world'}

class Regist(Resource):
    def post(self):
        user = request.json
        # if len(user) != 3:
        #     return {'status':'error'}
        username = user['username']
        email = user['email']
        password = user['password']

        db.session.add(User.User(username, email, password))
        db.session.commit()
        return User.result(200, 'success')



api.add_resource(Login, '/login')
api.add_resource(Regist, '/regist')