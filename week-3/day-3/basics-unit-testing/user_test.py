import unittest
from app_user import AppUser, InvalidUserNameException


class UserTest(unittest.TestCase):

    def test_check_user_non_null(self):
        dtc = dict()
        self.assertIsNotNone(dtc)

    def test_valid_user_name_length(self):
        user_name = 'abcdefghijklmn'
        password = '1333254'

        user = AppUser(user_name, password)
        self.assertEqual(user.user_name, 'abcdefghijklmn')

    def test_invalid_user_name_length(self):
        with self.assertRaises(InvalidUserNameException):
            user_name = 'abc'
            password = '1333254'

            AppUser(user_name, password)

    def test_invalid_user_name_at(self):
        with self.assertRaises(InvalidUserNameException):
            user_name = 'abc@bbbcrrr'
            password = '1333254'

            AppUser(user_name, password)

    def test_valid_user_name_at(self):
        user_name = 'abc12345678'
        password = '1333254'
        usr = AppUser(user_name, password)
        self.assertEqual(usr.user_name, 'abc12345678')


if __name__ == '__main__':
    unittest.main()
