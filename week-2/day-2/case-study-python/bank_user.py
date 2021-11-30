'''
This class represents user of the software. 
It can be admin or normal user.
'''


class BankUser:
    def __init__(
        self,
        user_name: str,
        password: str,
        role: str
    ) -> None:
        self.user_name = user_name
        self.password = password
        self.role = role
