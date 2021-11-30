'''
Holds the data and performs the bank operations, 
which are mentioned as features.
'''

from typing import List
from bank_account import BankAccount
from users import UserDatabase
import string
import random


class Bank:

    def __init__(self) -> None:
        self._accounts = []
        self.udb = UserDatabase()

    def create_bank_account(self, **kwargs) -> BankAccount:
        user_id = kwargs.get('user_id')
        ac_num = self.generate_account_number()
        # this code is written just to show you next operation
        ac = self.udb.get_user_by_id(user_id)

        ba: BankAccount = BankAccount(ac_num, ac)
        self._accounts.append(ba)
        return ba

    def check_balance(source: BankAccount) -> int: pass

    def transfer_money(
        source: BankAccount,
        target: BankAccount,
        amt: int
    ) -> bool: pass

    def withdraw(
        source: BankAccount,
        amt: int
    ) -> int: pass

    def deposit(
        source: BankAccount,
        amt: int
    ) -> int: pass

    def activate_account(source: BankAccount) -> None: pass

    def de_activate_account(source: BankAccount) -> None: pass

    def generate_account_number(self) -> str:
        return ''.join(
            random.choices(
                string.ascii_uppercase + string.digits, k=16
            )
        )

    def all_accounts(self) -> List[BankAccount]:
        return self._accounts
