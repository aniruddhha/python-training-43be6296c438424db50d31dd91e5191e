'''
    This class represents user of the software. 
    It can be admin or normal user.
'''


class BankUser:
    def __init__(
        self,
        id: int,
        user_name: str,
        password: str,
        role: str
    ) -> None:
        self.id = id
        self.user_name = user_name
        self.password = password
        self.role = role
