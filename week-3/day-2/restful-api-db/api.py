from flask import Flask, request
from flask_restful import Resource, Api
from db.connectivity import Connectivity
from resource.car import Car

con = Connectivity()  # connection should be initilized only once

app = Flask(__name__)

api = Api(app)

api.add_resource(
    Car,
    '/car',
    resource_class_kwargs={'db': con.db}
)


if __name__ == '__main__':
    app.run(debug=True)
