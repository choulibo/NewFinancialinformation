# coding = utf-8
import redis
from flask import Flask, session
from flask_migrate import Migrate, MigrateCommand
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask.ext.wtf import CSRFProtect
from config import Config



app = Flask(__name__)
app.config.from_object(Config)
manager = Manager(app)
# 初始化数据库
db = SQLAlchemy(app)
Migrate(app, db)
manager.add_command('db', MigrateCommand)
# 从配置对象中加载


# 初始化redis 存储对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# CSRF保护,只做服务器验证
CSRFProtect(app)
# 设置session保存指定位置
Session(app)


@app.route('/')
def index():
    session["name"] = "itlife"
    return 'indexnihao'


if __name__ == '__main__':
    manager.run()
