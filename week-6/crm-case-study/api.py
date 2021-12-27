from flask import Flask, request
from flask_restful import Api, Resource

from crm_admin.crm_admin_resource import CrmAdminResource
from customer.customer_manipulation_resource import CustomerManipulationResource
from customer.customer_mobile_availability import CustomerMobileAvailabilityResource
from customer.customer_fetch_resource import ListCustomerByAge, ListCustomerByLocation

app = Flask(__name__)

api = Api(app)

api.add_resource(CrmAdminResource, '/admin')

api.add_resource(CustomerManipulationResource, '/customer')
api.add_resource(CustomerMobileAvailabilityResource,
                 '/customer/mobile/<mobile:str>')
api.add_resource(ListCustomerByAge,
                 '/customer/age/<minAge:int>/<maxAge:int>')
api.add_resource(ListCustomerByAge, '/customer/location/<location:str>')


if __name__ == '__main__':
    app.run(debug=True)
