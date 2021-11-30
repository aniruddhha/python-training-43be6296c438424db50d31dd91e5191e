from typing import List
from bank_user import BankUser


class UserDatabase:
    def __init__(self) -> None:
        self._users = [
            BankUser('abc', 'abc', 'user'),
            BankUser('pqr', 'pqr', 'admin'),
        ]

    def allUsers(self) -> List[BankUser]:
        return self._users

# python users.py 

if __name__ == '__main__':
    udb: UserDatabase = UserDatabase()
    for user in udb.allUsers():
        print(f'{user.user_name}, {user.password}, {user.role}')
