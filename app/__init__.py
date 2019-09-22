# --*-- coding: utf-8 --*--
# @Author: zhang
# @Email: your email
# @Time: 2019/9/17 20:40
# @File: __init__.py
# @Software: PyCharm
# desc:app的构造函数
from flask import Flask


from app.models import init_model
from app.settings import DevConfig
from app.views import init_view
from app.views.views import blue

def create_app():
    #app创建
    app = Flask(__name__)

    #数据库信息配置
    app.config.from_object(DevConfig())

    #各模块的构建
    init_view(app=app)
    init_model(app=app)

    return app