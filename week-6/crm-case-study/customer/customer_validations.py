import datetime
from customer.customer_exceptions import *


def is_mobile_valid(mobile: str) -> bool:
    if(len(mobile) != 10):
        raise InvalidCustomerMobileException(
            'Mobile Length Should equals to 10'
        )
    return True


def is_name_valid(name: str):
    if(len(name) < 8):
        raise InvalidCustomerNameException(
            'Name should be min 8 character long'
        )
    return True


def is_email_valid(email: str): pass
def is_dob_valid(dob: datetime): pass
def is_location_valid(loc: str): pass
def is_status_vald(status: str): pass


def is_customer_valid(customer: dict):
    return is_mobile_valid(
        customer.get('mobile')
    ) and is_name_valid(
        customer.get('name')
    )
