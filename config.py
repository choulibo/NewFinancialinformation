# coding = utf-8
import logging
from redis import StrictRedis


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
    # 指定session 保存的redis
    SESSON_REDIS = StrictRedis(host = REDIS_HOST,port = REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2
    # 设置日志等级
    LOG_LEVEL = logging.DEBUG


class DevelopmentConfig(Config):
    """开发环境下的配置"""
    DEBUG = True

class ProductionConfig(Config):
    """生产环境下的配置"""
    DEBUG = False
    LOG_LEVEL = logging.WARNING


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


config = {
    "development":DevelopmentConfig,
    "production":ProductionConfig,
    "testing":TestingConfig

}



