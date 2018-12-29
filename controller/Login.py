# author: MQS
# datetime:2018/12/29 11:16
# software: PyCharm
# desc:
from run import app
from flask_restful import Resource, Api

api = Api(app)

class Login(Resource):
    def post(self):
        return {'hello':'world'}


api.add_resource(Login, '/login')