from flask_restful import Resource
from flask import request

from crm_user.user_activation_service import UserActivationService
from crm_user.user_exceptions import UnAuthorizedOperationException, UserAlreadyActivatedException, UserNotFoundException


class UserActivationResource(Resource):

    def __init__(
        self,
        activation_service: UserActivationService
    ) -> None:
        self.service = activation_service

    def put(self):
        req_obj: dict = request.get_json()

        try:
            op_res = self.service.activate_deactivate_user(
                req_obj.get('admin_id'),
                req_obj.get('user_id'),
                req_obj.get('sts')
            )

            return {
                'sts': 'success',
                'msg': f"{req_obj.get('user_id')} activated successfully",
                'res': op_res
            }
        except UnAuthorizedOperationException as ex:
            return {
                'sts': 'unauthorized',
                'msg': ex.msg,
                'res': 'operation failed'
            }, 403
        except UserNotFoundException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'not found'
            }, 404
        except UserAlreadyActivatedException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'already activated'
            }, 400
