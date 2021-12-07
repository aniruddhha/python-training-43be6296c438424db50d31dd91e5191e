from flask import Flask, request
from flask_restful import Api, Resource
import jwt

app = Flask(__name__)


@app.before_request
def before_all_requests():
    print('This is called')
    print(request.headers)
    print(type(request.headers))
    print(request.headers.get('sdldkfjskldf'))
    if('sdldkfjskldf' not in request.headers):
        return {
            'sts': 'unauthorized',
            'msg': 'you need to pass token'
        }, 401


@app.after_request
def after_all_requests(): pass


api = Api(app)


class Bank(Resource):
    def get(self):
        return {
            'sts': 'success',
            'msg': 'balance api',
            'res': 200
        }


class AppUser(Resource):
    def post(self):
        user_dict = request.get_json()

        if(user_dict.get('user_name') == 'abc' and user_dict.get('password') == 'abc'):
            secrete = '0123456789sdfsdf'
            algorithm = 'HS256'
            return {
                'sts': 'success',
                'msg': 'user validated successfully',
                'res': jwt.encode(user_dict, secrete, algorithm)
            }
        else:
            return {
                'sts': 'fail',
                'msg': 'User Not Available',
            }, 404


api.add_resource(AppUser, '/auth')
api.add_resource(Bank, '/bank')

if __name__ == '__main__':
    app.run(debug=True)
