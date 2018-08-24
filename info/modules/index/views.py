# coding = utf-8
from info import redis_store
from . import index_blu

# 创建路由
@index_blu.route("/")
def index():
    redis_store.set("name","itcast")
    return "index"


