'''
    - post the json with os, version, name and date key
    - date must be less that today -> throw custom exception InvalidDateException
'''

from flask import Flask, request
import datetime

from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


def is_date_less_than_today(dt: str):

    try:
        date_obj = datetime.date.fromisoformat(dt)
        today = datetime.date.today()
        if date_obj >= today:
            raise InvalidDateException('Date Should Be Less Than Today')

    except ValueError:
        raise

    except InvalidDateException:
        raise


class InvalidDateException(Exception):
    def __init__(self, msg: str) -> None:
        super().__init__(msg)


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


api.add_resource(Hello, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
