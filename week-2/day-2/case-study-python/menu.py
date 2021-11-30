'''
Responsible for displaying system menu.
'''
from users import UserDatabase
from bank import Bank


class Menu:

    def __init__(self) -> None:
        self.udb = UserDatabase()
        self.bank = Bank()
        self.user_id = ''

    def display_main_menu(self) -> None:
        print('''
        \n --- Main Menu ---
        1. Admin
        2. User
        3. Exit
        ''')

    def display_user_menu(self) -> None:
        print('''
        \n --- User Menu --- :
        1. Display Balance
        2. Transfer
        3. Withdraw
        4. Deposit
        5. Back
        ''')

    def display_admin_menu(self) -> None:
        print('''
        \n --- Admin Menu ---
        1. Create Account
        2. All Accounts
        3. Display Balance
        4. Transfer
        5. Withdraw
        6. Deposit
        7. Status
        8. Back
        ''')

    def display_status_sub_menu(self) -> None:
        print('''
        \n --- Manage Account Status ---
        1. Activate
        2. De-Activate
        3. Back
        ''')

    def cli_input(self, which: int) -> int:
        if which == 1:
            self.display_main_menu()
        elif which == 2:
            self.display_admin_menu()
        elif which == 3:
            self.display_user_menu()
        else:
            self.display_status_sub_menu()

        try:
            ch: int = int(input('Enter Your Choice : '))
        except:
            ch = 0
        return ch

    def cli_input_admin(self) -> None:
        ch: int = self.cli_input(2)
        if(ch == 1):
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
        elif ch == 2:
            for ac in self.bank.all_accounts():
                print(f'{ac._ac_num}\t {ac._balance} \t {ac._is_active}')
        elif ch == 8:
            return
        elif(ch == 7):
            self.cli_input_status()

    def cli_input_user(self) -> None:
        ch: int = self.cli_input(3)
        if(ch == 5):
            return

    def cli_input_status(self) -> None:
        ch: int = self.cli_input(4)
        if(ch == 3):
            self.cli_input(2)

    def cli(self) -> None:
        while True:
            ch: int = self.cli_input(1)
            if(ch == 1):
                self.admin_authentication()
            elif (ch == 2):
                self.user_authentication()
            elif ch == 0:
                print('\n Please Enter Numbers only')
            else:
                exit(0)

    def admin_authentication(self) -> bool:
        user_name = input('User Name : ')
        password = input('Password : ')
        if(
            self.udb.check_user_credentials(
                user_name=user_name,
                password=password,
                role='admin'
            )
        ):
            self.cli_input_admin()
        else:
            print('Un Authorized Admin')

    def user_authentication(self) -> bool:
        user_name = input('User Name : ')
        password = input('Password : ')
        if(
            self.udb.check_user_credentials(
                user_name=user_name,
                password=password,
                role='user'
            )
        ):
            self.cli_input_user()
        else:
            print('Un Authorized user')
