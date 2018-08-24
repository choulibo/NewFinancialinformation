# coding = utf-8
import logging

from flask import Flask, session
from flask_migrate import Migrate, MigrateCommand
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask.ext.wtf import CSRFProtect

from info import db, create_app,models

# manage.py 是程序启动的入口，只关心启动的相关参数及内容；
# 不关心具体创建app或者相关的逻辑


app = create_app("development")
manager = Manager(app)
# 将app 与db关联
Migrate(app, db)
#　将迁移命令添加到manager 中
manager.add_command('db', MigrateCommand)





if __name__ == '__main__':
    manager.run()
