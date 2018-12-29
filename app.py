from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Manager




app = Flask(__name__)

# 导入配置文件
app.config.from_object(Config)

# 建立数据库连接
db = SQLAlchemy(app)
# manager = Manager(app)

from controller import Login

if __name__ == '__main__':
    app.run()
