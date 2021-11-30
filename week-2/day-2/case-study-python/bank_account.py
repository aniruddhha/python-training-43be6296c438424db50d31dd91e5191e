from bank_user import BankUser


class BankAccount:
    def __init__(self, ac_num: str, user: BankUser) -> None:
        self._ac_num = ac_num
        self._user = user
        self._balance = 0
        self._is_active = False

    def set_balance(self, amt: int) -> None:
        self._balance = amt

    def get_balance(self) -> int:
        return self._balance

    def activate_account(self) -> None:
        self._is_active = True

    def de_activate_account(self) -> None:
        self._is_active = False
