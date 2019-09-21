# --*-- coding: utf-8 --*--
# @Author: zhang
# @Email: your email
# @Time: 2019/9/18 14:44
# @File: settings.py
# @Software: PyCharm
# desc:

class baseConfig:
    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(baseConfig):
    DEBUG = True
    dbinfo = {

        "ENGINE": "mysql",
        "USER": "root",
        "PSW": "123456",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flask-test",
    }

    SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}:{}/{}".format(dbinfo.get("ENGINE"),
                                                                dbinfo.get("USER"),
                                                                dbinfo.get("PSW"),
                                                                dbinfo.get("HOST"),
                                                                dbinfo.get("PORT"),
                                                                dbinfo.get("NAME"))

class TestConfig(baseConfig):
    DEBUG = True
    dbinfo = {

        "ENGINE": "mysql",
        "USER": "root",
        "PSW": "123456",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flask-test",
    }

    SQLALCHEMY_DATABASE_URI = "{}://{}:{}@{}:{}/{}".format(dbinfo.get("ENGINE"),
                                                                dbinfo.get("USER"),
                                                                dbinfo.get("PSW"),
                                                                dbinfo.get("HOST"),
                                                                dbinfo.get("PORT"),
                                                                dbinfo.get("NAME"))