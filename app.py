from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# from flask_migrate import Manager




app = Flask(__name__)

CORS(app, supports_credentials = True)

# 导入配置文件
app.config.from_object(Config)

# 建立数据库连接
db = SQLAlchemy(app)
# manager = Manager(app)

import route

if __name__ == '__main__':
    app.run()