
from flask import Flask, request
from flask_restful import Resource


class Mobile(Resource):
    def post(self):
        obj = request.get_json()
        if(not isinstance(obj, list)):
            return {
                'sts': 'fail',
                'msg': 'you must supply mobiles in list format []'
            }, 400
        return {
            'sts': 'wip',
            'msg': 'imcomplete api',
        }, 201
