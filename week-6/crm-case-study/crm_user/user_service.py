from pymysql.connections import Connection
from pymysql.cursors import Cursor

from crm_user.user_exceptions import UserNotFoundException


class UserService:
    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def perform_login(self, mobile: str, password: str) -> dict:

        csr: Cursor = self.db.cursor()
        sql = 'select * from crm_user where mobile = %s and password = %s'
        csr.execute(sql, (mobile, password))
        user = csr.fetchone()
        csr.close()

        if user != None:
            del user['password']
            return user

        raise UserNotFoundException('You are entering wrong credentials')
