from typing import List
from bank_user import BankUser
import random


class UserDatabase:
    def __init__(self) -> None:
        self._users = [  # instance variable
            BankUser(1, 'abc', 'abc', 'user'),
            BankUser(2, 'pqr', 'pqr', 'admin'),
        ]

    def all_users(self) -> List[BankUser]:
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

    def get_user_by_id(self, id: int) -> BankUser:
        return next((x for x in self._users if x.id == id), None)

    def create_new_user(self, **kwargs):
        user_name = kwargs.get('user_name')
        password = kwargs.get('password')
        role = kwargs.get('role')
        id = random.randint(0, 999)

        bu = BankUser(id, user_name, password, role)
        self._users.append(bu)

        return bu
