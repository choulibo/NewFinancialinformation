# coding = utf-8
import logging

from flask import Flask, session
from flask_migrate import Migrate, MigrateCommand
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

from flask_script import Manager
from flask.ext.wtf import CSRFProtect

from info import db, create_app


app = create_app("development")
manager = Manager(app)
# 将app 与db关联
Migrate(app, db)
#　将迁移命令添加到manager 中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session["name"] = "itlife"
    logging.debug("测试debug")
    logging.warning("测试dwarning")
    logging.error("测试error")
    logging.fatal("测试fatal")

    return 'indexnihao'


if __name__ == '__main__':
    manager.run()
