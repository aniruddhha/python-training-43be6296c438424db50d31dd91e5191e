from flask_restful import Resource
from flask import request


class UserManipulationResource(Resource):
    def get(self):
        req_body = request.get_json()

        pass
