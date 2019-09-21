# --*-- coding: utf-8 --*--
# @Author: zhang
# @Email: your email
# @Time: 2019/9/17 20:40
# @File: models.py
# @Software: PyCharm
# desc:
from app.models import db


# class BaseClass(db.Model):
#
#     def save(self):
#         db.session.add(self)
#         db.session.commit()
#         return self
#
#     def update(self,baseclass):
#         baseclass  = baseclass.__dict__
#         for k,v in baseclass:
#             if v :
#                 db.session.query(self).filter().update({k:v})
#         db.session.commit()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(14), nullable= False)
    psd = db.Column(db.String(256), nullable= False)

    def __init__(self,username,psd):
        self.username = username
        self.psd = psd

    def __repr__(self):
        return '[username:{},psd:{}]'.format(self.username,self.psd)

    def __str__(self):
        return '[username:{},psd:{}]'.format(self.username,self.psd)


