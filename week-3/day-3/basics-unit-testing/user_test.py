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


if __name__ == '__main__':
    unittest.main()
