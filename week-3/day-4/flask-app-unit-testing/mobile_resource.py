
from typing import List
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

        if(len(obj) != len(set(obj))):
            return {
                'sts': 'fail',
                'msg': 'unique mobiles are required'
            }, 400

        for mb in obj:
            if(len(mb) != 10):
                return {
                    'sts': 'fail',
                    'msg': f'mobile {mb} is not 10 digit long',
                }, 400
            if(any(not ch.isdigit() for ch in mb)):
                return {
                    'sts': 'fail',
                    'msg': f'mobile {mb} is not a mobile number',
                }, 400
        return {
            'sts': 'success',
            'msg': 'added mobile successfully',
            'res': obj
        }, 201
