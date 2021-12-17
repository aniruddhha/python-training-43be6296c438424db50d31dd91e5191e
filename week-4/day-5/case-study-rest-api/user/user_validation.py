from user.user_exception import *


class UserValidation:

    def is_user_valid(self, user: dict) -> bool:
        if(not set(user.keys()).issubset(('user_name', 'password', 'role', 'user_id'))):
            raise InvalidUserException('send required keys only')
        try:
            self.is_user_name_valid(user.get('user_name'))
            self.is_password_valid(user.get('password'))
            self.is_role_valid(user.get('role'))
            return True
        except:
            raise

    def is_password_valid(self, password: str) -> bool:
        if(len(password) < 8):
            raise InvalidPasswordException(
                'password should be 8 character long')
        return True

    def is_user_name_valid(self, user_name: str) -> bool:

        if(len(user_name) < 8):
            raise InvalidUserNameException(
                'username should be 8 character long')
        return True

    def is_role_valid(self, role: str) -> bool:
        if(role not in ['admin', 'user']):
            raise InvalidRoleException('roles should be either admin or user')
        return True
