from flask_restful import Resource


class Car(Resource):
    def __init__(self, db):
        self.db = db

    def post(self): pass

    def update(self): pass

    def delete(self): pass

    def get(self): pass
