# coding = utf-8
import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect

app = Flask(__name__)


class Config(object):
    """工程配置信息"""
    DEBUG = True
    SECRET_KEY = "jDk1CX4rp/c7uo2jr2GbrMST+ZKLGtVMFHVKSaCoammRmn4NXWsE90MCLis6/LJ"

    # 为数据库添加配置
    SQLALCHEMY_DATABASE_URI = "mysql:root:root@127.0.0.1:3306/information17"
    SQLALCHEMY_TRACK_MODIFYTION = False
    # redis 配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = "6379"
    # flask_session 的配置信息
    SESSION_TYPE = "redis"  # 指定session保存在redis中
    # 开启session签名
    SESSION_USE_SIGNER = True
    # 设置需要过期
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = 86400 * 2


# 从配置对象中加载
app.config.from_object(Config)
# 初始化数据库
db = SQLAlchemy(app)
# 指定session保存到redis
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# CSRF保护,只做服务器验证
CSRFProtect(app)
# 设置session保存指定位置
Session(app)


@app.route('/')
def index():
    return 'indexnihao'


if __name__ == '__main__':
    session["name"] = "itlife"
    app.run(debug=True)
