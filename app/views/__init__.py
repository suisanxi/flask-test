# --*-- coding: utf-8 --*--
# @Author: zhang
# @Email: your email
# @Time: 2019/9/17 21:13
# @File: __init__.py.py
# @Software: PyCharm
# desc:
from flasgger import Swagger
from flask_restful import Api

from app.views.restViews import UserView
from .views import blue

def init_view(app):
    app.register_blueprint(blue)

    #swagger 启动
    swagger = Swagger(app)

    #restful 路由管理
    api = Api(app)
    api.add_resource(UserView, '/rest')