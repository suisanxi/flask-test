# --*-- coding: utf-8 --*--
# @Author: zhang
# @Email: your email
# @Time: 2019/9/17 20:40
# @File: __init__.py
# @Software: PyCharm
# desc:
from flask import Flask


from app.models import init_model
from app.settings import DevConfig
from app.views import init_view
from app.views.views import blue

def create_app():
    app = Flask(__name__)


    app.config.from_object(DevConfig())

    init_view(app=app)
    init_model(app=app)

    return app