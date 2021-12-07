from flask import Flask, request
from flask_restful import Resource, Api
from db.connectivity import Connectivity

con = Connectivity()

app = Flask(__name__)

api = Api(app)


if __name__ == '__main__':
    app.run(debug=True)
