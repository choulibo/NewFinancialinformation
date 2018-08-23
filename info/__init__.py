# coding = utf-8
import redis
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

from config import config

app = Flask(__name__)
# 从配置对象中加载
app.config.from_object(config["development"])
# 初始化数据库
db = SQLAlchemy(app)

# 初始化redis 存储对象
redis_store = redis.StrictRedis(host=config["development"].REDIS_HOST, port=config["development"].REDIS_PORT)
# CSRF保护,只做服务器验证
CSRFProtect(app)
# 设置session保存指定位置
Session(app)