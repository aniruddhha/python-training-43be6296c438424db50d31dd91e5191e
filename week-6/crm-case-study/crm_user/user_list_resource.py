from flask_restful import Resource
from flask import request

from crm_user.user_list_service import UserListService



class UserListResource(Resource):

    def __init__(self, service: UserListService) -> None:
        self.service = service

    def get(self):

        return {
            'sts': 'success',
            'msg': 'all users in db',
            'res': self.service.list_all_users()
        }
