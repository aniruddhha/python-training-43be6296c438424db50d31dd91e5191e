'''
Holds the data and performs the bank operations, 
which are mentioned as features.
'''

from bank_account import BankAccount


class Bank:

    def create_bank_account() -> BankAccount: pass

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
