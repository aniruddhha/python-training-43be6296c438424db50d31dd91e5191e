from flask_restful import Resource
from flask import request
from customer.customer_service import CustomerService
from customer.customer_exceptions import *


class CustomerManipulationResource(Resource):
    def __init__(self, service: CustomerService) -> None:
        super().__init__()
        self.service = service

    def create_new_customer(self):
        customer = request.get_json()

        try:
            cnt = self.service.save_customer(customer)
            return {
                'sts': 'success',
                'msg': 'customer saved successfully',
                'res': f'{cnt}'
            }, 201
        except InvalidCustomerMobileException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'Invalid Mobile Number'

            }, 400
        except InvalidCustomerNameException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'Invalid Name'
            }, 400

    def update_customer(self): pass
