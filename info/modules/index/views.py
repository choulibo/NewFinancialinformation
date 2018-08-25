# coding = utf-8
from flask import render_template, current_app

from info import redis_store
from . import index_blu


# 创建路由
@index_blu.route('/')
def index():
    return render_template('news/index.html')

# send_static_file 是flask 去查找指定文件的静态文件所调用的方法
@index_blu.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/favicon.ico')