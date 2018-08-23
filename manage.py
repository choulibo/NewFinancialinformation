# coding = utf-8
import redis
from flask import Flask, session
from flask_migrate import Migrate, MigrateCommand
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask.ext.wtf import CSRFProtect


class Config(object):
    """工程配置信息"""
    DEBUG = True
    SECRET_KEY = "jDk1CX4rp/c7uo2jr2GbrMST+ZKLGtVMFHVKSaCoammRmn4NXWsE90MCLis6/LJ"

    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/information17"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis 配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"

    # Session 的配置信息
    SESSION_TYPE = "redis"  # 指定session保存在redis中
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2


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
