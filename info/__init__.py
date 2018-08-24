# coding = utf-8
from logging.handlers import RotatingFileHandler
import logging
import redis
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from config import config

db = SQLAlchemy()


def setup_log(config_name):
    # 设置日志的记录等级
    logging.basicConfig(level=config[config_name].LOG_LEVEL)  # 调试debug级日志文件个数上限
    # 创建日志记录器，指明日志保存的路径每个日志文件的大小，保存的
    file_log_handler = RotatingFileHandler('logs/log', maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式，日志等级，输入日志信息的文件名　行数　日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)

def create_app(config_name):
    # 配置日志并且传入配置名字，以便能获取到指定配置所对应的日志等级
    setup_log(config_name)
    # 创建flask 对象
    app = Flask(__name__)
    # 从配置对象中加载
    app.config.from_object(config[config_name])
    # 初始化数据库
    # 通过app初始化
    db.init_app(app)

    # 初始化redis 存储对象
    redis_store = redis.StrictRedis(host=config[config_name].REDIS_HOST, port=config[config_name].REDIS_PORT)
    # CSRF保护,只做服务器验证
    CSRFProtect(app)
    # 设置session保存指定位置
    Session(app)

    return app
