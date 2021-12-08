import unittest
from app_user import AppUser, InvalidUserNameException, InvalidPasswordException


class UserTest(unittest.TestCase):

    def test_check_user_non_null(self):
        dtc = dict()
        self.assertIsNotNone(dtc)

    def test_valid_user_name_length(self):
        user_name = 'Abcdefghijklmn'
        password = '133$32#54'

        user = AppUser(user_name, password)
        self.assertEqual(user.user_name, 'Abcdefghijklmn')

    def test_invalid_user_name_length(self):
        with self.assertRaises(InvalidUserNameException):
            user_name = 'abc'
            password = '1$33#3254'

            AppUser(user_name, password)

    def test_invalid_user_name_at(self):
        with self.assertRaises(InvalidUserNameException):
            user_name = 'Abc@bbbcrrr'
            password = '1#333$254'

            AppUser(user_name, password)

    def test_valid_user_name_at(self):
        user_name = 'Abc12345678'
        password = '1#333$254'
        usr = AppUser(user_name, password)
        self.assertEqual(usr.user_name, 'Abc12345678')

    def test_valid_user_name_upper(self):
        user_name = 'Abc12345678'
        password = '1333$54#'
        usr = AppUser(user_name, password)
        self.assertEqual(usr.user_name, 'Abc12345678')

    def test_invalid_user_name_lower(self):
        with self.assertRaises(InvalidUserNameException):
            user_name = 'accccccccccccc'
            password = '$1333#254'

            AppUser(user_name, password)

    def test_invalid_password_hash_dollar(self):
        with self.assertRaises(InvalidPasswordException):
            user_name = 'Accccccccccccc'
            password = '1333254'

            AppUser(user_name, password)

    def test_valid_password_hash_dollar(self):
        user_name = 'Accccccccccccc'
        password = '$1333254#'

        usr = AppUser(user_name, password)
        self.assertEqual(usr.password, '$1333254#')


if __name__ == '__main__':
    unittest.main()
