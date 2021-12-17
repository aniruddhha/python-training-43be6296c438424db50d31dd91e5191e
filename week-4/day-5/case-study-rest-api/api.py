from flask import Flask, request
from flask_restful import Api, Resource

from user.user_resource import UserResource
from db.connectivity import Connectivity

app = Flask(__name__)
api = Api(app)
connection = Connectivity().db  # for maintaining single db connection

api.add_resource(
    UserResource,  # shape of user resource
    '/user',
    resource_class_kwargs={'db': connection}  # imp step
)

if __name__ == '__main__':
    app.run(debug=True)
