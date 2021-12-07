from flask import Flask, request
from flask_restful import Api, Resource
import jwt

app = Flask(__name__)

api = Api(app)


class AppUser(Resource):
    def post(self):
        user_dict = request.get_json()

        if(user_dict.get('user_name') == 'abc' and user_dict.get('password') == 'abc'):
            secrete = '0123456789'
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

if __name__ == '__main__':
    app.run(debug=True)
