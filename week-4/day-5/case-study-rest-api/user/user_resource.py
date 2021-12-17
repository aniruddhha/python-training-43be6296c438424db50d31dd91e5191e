from flask_restful import Resource
from flask import request

from pymysql.cursors import Cursor
from pymysql.connections import Connection

from user.user_validation import UserValidation
from user.user_exception import *


class UserResource(Resource):

    def __init__(self, db: Connection):
        self.db = db
        self.validation = UserValidation()

    def get(self):
        csr: Cursor = self.db.cursor()
        sql = 'select * from app_user'
        csr.execute(sql)
        users = csr.fetchall()
        csr.close()

        return {
            'sts': 'success',
            'msg': 'users in a database',
            'res': users
        }

    def post(self):
        user = request.get_json()
        try:
            self.validation.is_user_valid(user)
            csr: Cursor = self.db.cursor()
            self.db.begin()
            sql = 'insert into app_user values(%(user_id)s, %(user_name)s, %(password)s, %(role)s)'
            cnt = csr.execute(sql, user)
            self.db.commit()
            csr.close()

            return {
                'sts': 'success',
                'msg': 'user created successfully',
                'res': cnt
            }
        except InvalidUserNameException as ex:
            return {
                'sts': 'fail',
                'msg': ex.__str__()
            }, 400
        except InvalidPasswordException as ex:
            return {
                'sts': 'fail',
                'msg': ex.__str__()
            }, 400
        except InvalidRoleException as ex:
            return {
                'sts': 'fail',
                'msg': ex.__str__()
            }, 400
