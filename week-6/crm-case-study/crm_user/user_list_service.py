from pymysql.connections import Connection
from pymysql.cursors import Cursor

from date_util.date_to_json import convert_object_to_dict_which_contains_date


class UserListService:

    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def list_all_users(self) -> tuple:
        csr: Cursor = self.connection.cursor()

        sql: str = 'select mobile, doj, role, status from crm_user'
        csr.execute(sql)
        users: tuple = csr.fetchall()  # tuple of users dictionary which contains date object

        users_converted = map(
            convert_object_to_dict_which_contains_date,
            users
        )  # we converted above tuple to tuple of dictionaries with date as a string and not date object

        csr.close()

        return list(users_converted)
