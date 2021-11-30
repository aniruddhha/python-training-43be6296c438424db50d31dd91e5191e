from bank_user import BankUser


class BankAccount:
    def __init__(self, ac_num: str, user: BankUser) -> None:
        self._ac_num = ac_num
        self._balance = 0
        self._is_active = False
        self._user = user

    def set_balance(self, amt: int) -> None:
        self._balance = amt

    def get_balance(self) -> int:
        return self._balance

    def activate_account(self) -> None:
        self._is_active = True

    def de_activate_account(self) -> None:
        self._is_active = False

    def __str__(self) -> str:  # converts state into string representation
        return f'\n Ac # : {self._ac_num} \n Balance : {self._balance} \n Status : {self._is_active}'
