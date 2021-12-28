from flask import Flask, request
from flask_restful import Api, Resource

from crm_admin.crm_admin_resource import CrmAdminResource
from customer.customer_manipulation_resource import CustomerManipulationResource
from customer.customer_mobile_availability import CustomerMobileAvailabilityResource
from customer.customer_fetch_resource import ListCustomerByAgeResource, ListCustomerByLocationResource
from customer.customer_service import CustomerService

from database.connectivity import Connectivity

connection = Connectivity().db
service: CustomerService = CustomerService(connection)

app = Flask(__name__)

api = Api(app)

api.add_resource(
    CrmAdminResource,
    '/admin'
)

api.add_resource(
    CustomerManipulationResource,
    '/customer'
)

api.add_resource(
    CustomerMobileAvailabilityResource,
    '/customer/mobile/<mobile:str>'
)

api.add_resource(
    ListCustomerByAgeResource,
    '/customer/age/<minAge:int>/<maxAge:int>',
    resource_class_kwargs={'service': service}
)

api.add_resource(
    ListCustomerByLocationResource,
    '/customer/location/<location:str>',
    resource_class_kwargs={'service': service}
)

if __name__ == '__main__':
    app.run(debug=True)
