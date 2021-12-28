from flask_restful import Resource
from flask import request

from crm_user.user_service import UserService
from crm_user.user_exceptions import UserNotFoundException


class UserManipulationResource(Resource):
    def get(self, service: UserService):
        req_body:  dict = request.get_json()

        try:
            user = service.perform_login(
                req_body.get('user_name'),
                req_body.get('password'),
            )

            return {
                'sts': 'success',
                'msg': 'user logged in successfully',
                'res': user
            }
        except UserNotFoundException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
            }
