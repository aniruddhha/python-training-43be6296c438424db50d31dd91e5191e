import json

from date_util.date_to_json import convert_object_to_dict_which_contains_date, date_to_string
from flask_restful import Resource
from flask import request

from crm_user.user_service import UserService
from crm_user.user_exceptions import InActiveUserException, UserNotFoundException


class UserManipulationResource(Resource):

    def __init__(self,  service: UserService) -> None:
        super().__init__()
        self.service = service

    def post(self):
        req_body:  dict = request.get_json()

        try:
            user_raw = self.service.perform_login(
                req_body.get('user_name'),
                req_body.get('password'),
            )

            return {
                'sts': 'success',
                'msg': 'user logged in successfully',
                'res': convert_object_to_dict_which_contains_date(user_raw)
            }
        except UserNotFoundException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'user not found'
            }, 404
        except InActiveUserException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'inactive user'
            }, 403
