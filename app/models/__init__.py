# --*-- coding: utf-8 --*--
# @Author: zhang
# @Email: your email
# @Time: 2019/9/18 15:00
# @File: __init__.py.py
# @Software: PyCharm
# desc:

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_model(app):
    db.init_app(app)