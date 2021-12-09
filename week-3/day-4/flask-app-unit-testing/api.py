from flask import Flask

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


api.add_resource(Hello, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
