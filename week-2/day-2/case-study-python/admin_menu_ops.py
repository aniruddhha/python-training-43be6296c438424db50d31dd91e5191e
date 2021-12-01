from bank import Bank
from users import UserDatabase


class AdminMenuOperation:

    def __init__(self, udb: UserDatabase, bank: Bank) -> None:
        self.udb = udb
        self.bank = bank

    def create_bank_account(self):
        print('\n For Creating Bank Account Enter Following Details')
        user_name = input('\n Enter User Name : ')
        password = input('\n Enter Password : ')

        bu = self.udb.create_new_user(
            user_name=user_name,
            password=password,
            role='user'
        )

        ba = self.bank.create_bank_account(user_id=bu.id)
        print('\n --- Account Successfully Created ----')

        print(ba)

    def all_accounts(self):
        for ac in self.bank.all_accounts():
            print(f'{ac._ac_num}\t {ac._balance} \t {ac._is_active}')

    def deposit(self):
        print('\n For Deposit, Enter Following Details')
        ac_num = input('Enter AC Num : ')
        amt = int(input('Enter Amount : '))

        ac = self.bank.get_ac_by_num(ac_num)

        self.bank.deposit(ac, amt)
