'''
    - post the json with os, version, name and date key
    - date must be less that today -> throw custom exception InvalidDateException
'''

from flask import Flask, request
from flask.signals import request_started

from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Hello(Resource):
    def get(self):
        return {
            'os': 'android',
            'version': '11',
            'name':  'not-named'
        }

    def post(self):
        obj = request.get_json()
        return {
            'sts': 'success',
            'msg': 'os created successfully',
            'res': obj
        }, 201


api.add_resource(Hello, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
