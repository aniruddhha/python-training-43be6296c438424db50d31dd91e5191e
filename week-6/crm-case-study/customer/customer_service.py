import pymysql

from pymysql.connections import Connection
from pymysql.cursors import Cursor

from customer.customer_validations import *


# service class will make communication with database
class CustomerService:
    def __init__(self, connection: Connection):
        self.connection = connection

    def save_customer(self, customer: dict) -> int:

        try:
            sts = is_customer_valid(customer)
            if(sts):
                sql = 'insert into crm_customer values (%(mobile)s, %(name)s, %(email)s, %(dob)s, %(location)s, %(status)s )'
                csr: Cursor = self.connection.cursor()
                self.connection.begin()
                cnt = csr.execute(sql, customer)
                self.connection.commit()
                csr.close()
                return cnt
        except:
            raise

    def update_customer(self, customer: dict) -> int: pass
    def block_customer(self, customer_id: str) -> bool: pass
    def is_mobile_registered(self, mobile: str) -> bool: pass
    def list_customers_by_location(self, location: str) -> tuple: pass
    def list_customers_by_age(self, minAge: int, maxAge: int) -> tuple: pass
