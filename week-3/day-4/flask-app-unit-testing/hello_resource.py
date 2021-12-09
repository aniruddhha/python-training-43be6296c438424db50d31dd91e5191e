
from flask import Flask, request
from flask_restful import Resource
from app_date_util import is_date_less_than_today
from invalid_date_exception import InvalidDateException


class Hello(Resource):
    def get(self):
        return {
            'os': 'android',
            'version': 11,
            'name':  'not-named'
        }

    def post(self):
        obj = request.get_json()
        dt = obj.get('date')
        try:
            is_date_less_than_today(dt)
            return {
                'sts': 'success',
                'msg': 'os created successfully',
                'res': obj
            }, 201

        except ValueError:
            return {
                'sts': 'fail',
                'msg': 'Date Format Should be (YYYY-MM-DD)',
            }, 400
        except InvalidDateException:
            return {
                'sts': 'fail',
                'msg': 'Date Should be Less Than Today',
            }, 400
