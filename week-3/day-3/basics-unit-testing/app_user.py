
'''
    - username should be greater than 8 characters -> throw Exception
    - username should not contain @ character -> throw Exception
    - username must start from capital letter -> throw Exception
    - password must contain $ and # -> throw Exception
    - password should be greater than 8 characters -> throw Exception
    - password should not start from digit -> throw Exception
'''


class InvalidUserNameException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class InvalidPasswordException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class AppUser:
    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password

        self.validate()

    def validate(self):
        if(len(self.user_name) < 8):
            raise InvalidUserNameException(
                'Username must be greater than 8 characters')
        if('@' in self.user_name):
            raise InvalidUserNameException(
                'Username should not contain @')
        if(self.user_name[0].islower()):
            raise InvalidUserNameException(
                'Username must start from caps letter')
        if('$' not in self.password and '#' not in self.password):
            raise InvalidPasswordException(
                'password should contain $ and #')
