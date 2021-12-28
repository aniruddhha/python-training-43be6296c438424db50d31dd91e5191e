from customer.customer_manipulation_resource import CustomerManipulationResource
from customer.customer_mobile_availability import CustomerMobileAvailabilityResource
from customer.customer_fetch_resource import ListCustomerByAgeResource, ListCustomerByLocationResource
from customer.customer_service import CustomerService
from pymysql.connections import Connection


def load_customer_routes(api, connection: Connection):

    service: CustomerService = CustomerService(connection)

    api.add_resource(
        CustomerManipulationResource,
        '/customer'
    )

    api.add_resource(
        CustomerMobileAvailabilityResource,
        '/customer/mobile/<string:mobile>'
    )

    api.add_resource(
        ListCustomerByAgeResource,
        '/customer/age/<int:minAge>/<int:maxAge>',
        resource_class_kwargs={'service': service}
    )

    api.add_resource(
        ListCustomerByLocationResource,
        '/customer/location/<string:location>',
        resource_class_kwargs={'service': service}
    )
