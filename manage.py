# coding = utf-8
import redis
from flask import Flask, session
from flask_migrate import Migrate, MigrateCommand
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask.ext.wtf import CSRFProtect
from config import Config
from info import db, app

manager = Manager(app)
# 将app 与db关联
Migrate(app, db)
#　将迁移命令添加到manager 中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session["name"] = "itlife"
    return 'indexnihao'


if __name__ == '__main__':
    manager.run()
