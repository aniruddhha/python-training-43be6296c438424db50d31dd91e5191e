from typing import List
from bank_user import BankUser


class UserDatabase:
    def __init__(self) -> None:
        self._users = [  # instance variable
            BankUser('abc', 'abc', 'user'),
            BankUser('pqr', 'pqr', 'admin'),
        ]

    def allUsers(self) -> List[BankUser]:
        return self._users

    def check_user_credentials(self, **kwargs) -> bool:
        user_name = kwargs.get('user_name')
        password = kwargs.get('password')
        role = kwargs.get('role')

        sts: bool = False
        for user in self._users:
            if(user.user_name == user_name and user.password == password and user.role == role):
                sts = True
                break
            else:
                sts = False
        return sts
