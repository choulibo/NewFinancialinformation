# coding = utf-8


class config(object):
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



class DevelopmentConfig(config):
    """开发环境下的配置"""
    DEBUG = True

class ProductionConfig(config):
    DEBUG = False


class TestingConfig(config):
    DEBUG = True
    TESTING = True


config = {
    "development":DevelopmentConfig,
    "production":ProductionConfig,
    "testing":TestingConfig

}



