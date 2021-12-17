import unittest

from user.user_validation import UserValidation
from user.user_exception import *


class UserValidationTest(unittest.TestCase):

    def setUp(self) -> None:
        self.validation = UserValidation()

    def test_is_user_name_type_dict_valid(self):
        user = {
            'user_name': '123456789',
            'password': '123456789',
            'role': 'admin'
        }
        expected = True
        actual = self.validation.is_user_valid(user)
        self.assertEqual(expected, actual)

    def test_is_user_name_type_dict_invalid(self):
        with self.assertRaises(InvalidUserException):
            user = {
                'user_name': '123456789',
                'password': '123456789',
                'role': 'admin',
                'age': 12
            }

            self.validation.is_user_valid(user)
