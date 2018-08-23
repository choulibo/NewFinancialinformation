# coding = utf-8
from flask import Flask

app = Flask(__name__)

class Config(object):
    """工程配置信息"""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql:root:root@127.0.0.1:3306/information17"
    SQLALCHEMY_TRACK_MODIFYTION = False
# 从配置对象中加载
app.config.from_object(Config)


@app.route('/')
def index():
    return 'indexnihao'


if __name__ == '__main__':
    app.run(debug=True)
