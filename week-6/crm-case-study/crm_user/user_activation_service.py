from pymysql.connections import Connection
from pymysql.cursors import Cursor

from crm_user.user_exceptions import UnAuthorizedOperationException, UserAlreadyActivatedException, UserNotFoundException


class UserActivationService:

    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def activate_deactivate_user(
        self,
        admin_id: str,
        user_id: str,
        sts: int
    ) -> bool:

        csr: Cursor = self.connection.cursor()
        self.connection.begin()

        sql = 'select * from crm_user where mobile = %s'
        csr.execute(sql, (admin_id))
        user: dict = csr.fetchone()

        if(not user):
            raise UserNotFoundException(f'admin {user_id} not present')

        if user.get('role') != 'admin':
            raise UnAuthorizedOperationException(
                'only admin can perform activation')

        sql = 'select * from crm_user where mobile = %s'
        csr.execute(sql, (user_id))

        user: dict = csr.fetchone()
        if(not user):
            raise UserNotFoundException(f'user {user_id} not present')

        if(sts == 1 and user.get('status') == 1):
            raise UserAlreadyActivatedException(
                f'{user_id} already activated'
            )

        if(sts == 0 and user.get('status') == 0):
            raise UserAlreadyActivatedException(
                f'{user_id} already deactivated'
            )

        sql = 'update crm_user set status = %s where mobile = %s'
        cnt = csr.execute(sql, (sts, user_id))

        self.connection.commit()
        csr.close()

        return cnt
