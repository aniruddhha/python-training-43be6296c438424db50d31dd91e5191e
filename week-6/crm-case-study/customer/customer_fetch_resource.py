from flask_restful import Resource
from customer.customer_service import CustomerService


class ListCustomerByAgeResource(Resource):

    def __init__(self, service: CustomerService) -> None:
        super().__init__()
        self.service = service

    def get(self, minAge: int, maxAge: int):
        return {
            'sts': 'success',
            'res': self.service.list_customers_by_age(minAge, maxAge)
        }


class ListCustomerByLocationResource(Resource):
    def __init__(self, service: CustomerService) -> None:
        super().__init__()
        self.service = service

    def get(self, location: str):
        return {
            'sts': 'success',
            'res': self.service.list_customers_by_location(location)
        }
