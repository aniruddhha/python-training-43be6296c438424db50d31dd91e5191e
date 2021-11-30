'''
Responsible for displaying system menu.
'''


class Menu:

    def display_user_menu(self) -> None:
        print('''
            \n --- User Menu --- : 
            1. Display Balance
            2. Transfer
            3. Withdraw
            4. Deposit
            5. Exit
        ''')

    def display_main_menu(self) -> None:
        print('''
            \n --- Main Menu ---
            1. Admin
            2. User
            3. Exit
        ''')

    def display_admin_menu(self) -> None:
        print('''
            \n --- Admin Menu --- 
            1. Create Account
            2. Display Balance
            2. Transfer
            3. Withdraw
            4. Deposit
            5. Status
            6. Exit
        ''')

    def cli(self) -> None:
        while True:
            self.display_main_menu()
            ch: int = int(input('Enter Your Choice : '))

            if(ch == 1):
                self.display_admin_menu()
                ch: int = int(input('Enter Your Choice : '))
                if(ch == 6):
                    return
            elif (ch == 2):
                self.display_user_menu()
                ch: int = int(input('Enter Your Choice : '))
                if(ch == 5):
                    return
            else:
                exit(0)
