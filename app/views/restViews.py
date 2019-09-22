# --*-- coding: utf-8 --*--
# @Author: zhang
# @Email: your email
# @Time: 2019/9/19 9:01
# @File: restViews.py
# @Software: PyCharm
# desc:restful api+swagger接口编写
from flask import Blueprint
from flask_restful import Resource, fields, marshal_with
from flask_restful.reqparse import RequestParser

from app.models import db
from app.models.models import User




#返回的json格式
user_fields = {
    'id': fields.Integer,
    'username':fields.String,
    'psd':fields.String,
}

result = {
    'code': fields.Integer,
    'msg': fields.String,
    'data': fields.List(fields.Nested(user_fields))
}

result_simple = {
    'code': fields.Integer,
    'msg': fields.String,
    'data': fields.Nested(user_fields)
}
parser = RequestParser()


class UserView(Resource):
    @marshal_with(result)
    def get(self):

        """查用户列表的一个接口
        This is using docstrings for specifications.
        ---
        parameters:
          - name: id
            in: query
            type: int
            required: false
            default: null
        responses:
          200:
            description: 查询成功
        """
        parser.add_argument("id", type=int, location="args")
        args = parser.parse_args()
        id = args.get('id')
        if not id :
            user = User.query.all()
        else:
            user = User.query.get(id)
        #分页用下面的代码，但是返回的json格式要重新写
        # page = User.query.filter().paginate(page=2, per_page=2,error_out=False)
        # print(page.items,page.pages,page.pages)
        data = {
            'code':200,
            'msg':'查询成功',
            'data': user,
        }
        return  data

    @marshal_with(result)
    def post(self):
        """
        方法名称：增加用户
        方法描述：调用此API增加用户,把默认值复制下去，注意下
        ---

        parameters:
          - name: body
            in: body
            required: true
            default: '
            {
    "username": "asdf ",
    "psw": "asdg ",
    "user":[{
        "username":"asdf",
        "psd":"dsfgag"/n
    },{
        "username":"fgdh",
        "psd":"klgfhdgf"/n
    }]
}         '

        responses:
          200:
            description: 插入成功
               """
        parser.add_argument('username', type=str, help='你怎么忘填名字了o(´^｀)o')
        parser.add_argument('psw', type=str, help='你还能忘填密码了o(´^｀)o')
        parser.add_argument('user', type=User, action='append')
        args = parser.parse_args()
        username = args.get('username')
        psw = args.get('psw')
        u = args.get('user')
        if not username or not psw:
            return { 'code':400,'msg':'想什么呢，东西都能空'}
        user = User(username,psw)
        user.username = username
        user.psd = psw
        db.session.add(user)
        db.session.commit()
        return { 'code':200,'msg':'插入成功','data':user}

    @marshal_with(result_simple)
    def put(self):
        """
            方法名称：修改用户
            方法描述：id为对象主键，其他为对象属性
            ---

            parameters:
              - name: body
                in: body
                required: true
                default: '
                {
                    "id":7,
                    "username": "345326",
                    "psw": "34523452"
                } '

            responses:
              200:
                description: 修改成功
                   """
        parser.add_argument('id', type=int)
        parser.add_argument('username', type=str)
        parser.add_argument('psw', type=str)
        args = parser.parse_args()
        id = args.get('id')
        usernanme = args.get('username')
        psw = args.get('psw')
        u = User.query.get(id)
        print(type(u))
        if usernanme:
            u.username = usernanme
        if psw :
            u.psd = psw
        print('u:',u)
        db.session.commit()
        return { 'code':200,'msg':'修改成功','data':u}

    @marshal_with(result_simple)
    def delete(self):
        """
           方法名称：删除用户
           方法描述：id为对象主键，
           ---

           parameters:
             - name: body
               in: body
               required: true
               default: '
               {
                   "id":7
               } '

           responses:
             200:
               description: 修改成功
                  """
        parser.add_argument('id', type=int)
        args = parser.parse_args()
        id = args.get('id')
        user = User.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return {'code': 200, 'msg': '删除成功', 'data': user}


