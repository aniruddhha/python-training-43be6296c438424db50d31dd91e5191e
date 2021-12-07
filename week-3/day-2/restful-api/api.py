from flask import Flask
from flask_restful import Resource, Api  # new -> rest api

app = Flask(__name__)

api = Api(app)  # new -> rest api


class HelloWorld(Resource):
    def get(self):
        return {
            'sts': 'checking',
            'msg': 'checking flask restful extention',
            'res': 'GET'
        }

    def post(self):
        return {
            'sts': 'checking',
            'msg': 'checking flask restful extention',
            'res': 'POST'
        }


class ByeBye(Resource):
    def get(self):
        return {
            'sts': 'checking',
            'msg': 'checking flask restful extention',
            'res': 'GET'
        }


api.add_resource(HelloWorld, '/hello')
api.add_resource(ByeBye, '/bye')

if __name__ == '__main__':
    app.run(debug=True)
