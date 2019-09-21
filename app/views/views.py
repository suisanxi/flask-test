# --*-- coding: utf-8 --*--
# @Author: zhang
# @Email: your email
# @Time: 2019/9/17 20:40
# @File: views.py
# @Software: PyCharm
# desc:




# def init_route(app):
#     @app.route('/hello')
#     def hello_world():
#         return 'hello world'

from flask import Blueprint

from app.models import db

blue = Blueprint('blue',__name__)

@blue.route('/blue')
def index():
    return 'blue test'


@blue.route('/creat')
def creat():
    db.create_all()
    return "数据库以创建"