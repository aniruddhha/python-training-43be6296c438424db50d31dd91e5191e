from pymysql.connections import Connection
from pymysql.cursors import Cursor


class UserListService:

    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def list_all_users(self) -> tuple:
        csr: Cursor = self.connection.cursor()

        sql: str = 'select * from crm_user'
        csr.execute(sql)
        users: tuple = csr.fetchall()

        csr.close()

        return users
