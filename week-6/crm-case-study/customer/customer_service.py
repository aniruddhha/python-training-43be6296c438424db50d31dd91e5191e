import pymysql

from pymysql.connections import Connection


# service class will make communication with database
class CustomerService:
    def __init__(self, connection: Connection):
        self.connection = connection

    def save_customer(self, customer: dict) -> int: pass
    def update_customer(self, customer: dict) -> int: pass
    def block_customer(self, customer_id: str) -> bool: pass
    def is_mobile_registered(self, mobile: str) -> bool: pass
    def list_customers_by_location(self, location: str) -> tuple: pass
    def list_customers_by_age(self, minAge: int, maxAge: int) -> tuple: pass
