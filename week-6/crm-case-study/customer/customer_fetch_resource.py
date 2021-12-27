from flask_restful import Resource


class ListCustomerByAge(Resource):
    def get(self, minAge: int, maxAge: int): pass


class ListCustomerByLocation(Resource):
    def get(self, location: str): pass
