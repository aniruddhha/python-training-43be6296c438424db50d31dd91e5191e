from flask_restful import Resource
from flask import request

from user_activation_service import UserActivationService


class UserActivationResource(Resource):

    def __init__(self, service: UserActivationService) -> None:
        self.service = service

    def put(self):
        req_obj: dict = request.get_json()

        op_res = self.service.activate_user(
            req_obj.get('admin_id'),
            req_obj.get('user_id')
        )

        return {
            'sts': 'success',
            'msg': f"{req_obj.get('user_id')} activated successfully",
            'res': op_res
        }
