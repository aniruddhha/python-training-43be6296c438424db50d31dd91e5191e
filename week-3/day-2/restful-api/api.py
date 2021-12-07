from flask import Flask, request
from flask_restful import Resource, Api, reqparse  # new -> rest api

app = Flask(__name__)

api = Api(app)  # new -> rest api

# parser = reqparse.RequestParser()
# parser.add_argument('id', type=int)
# parser.add_argument('msg', type=str)


class HelloWorld(Resource):
    def get(self):
        return {
            'sts': 'checking',
            'msg': 'checking flask restful extention',
            'res': 'GET'
        }

    def post(self):

        # args = parser.parse_args()
        dt = request.get_json()

        return {
            'sts': 'checking',
            'msg': 'checking flask restful extention',
            'res': dt
        }


class ByeBye(Resource):
    def get(self, bye_id):
        return {
            'sts': 'checking',
            'msg': 'checking flask restful extention',
            'res': f'Bye Bye is {bye_id}'
        }

    def get(self):
        return {
            'sts': 'checking',
            'msg': 'checking flask restful extention',
            'res': 'Only Bye'
        }


api.add_resource(HelloWorld, '/hello')
api.add_resource(ByeBye, '/bye/<bye_id>')

if __name__ == '__main__':
    app.run(debug=True)
