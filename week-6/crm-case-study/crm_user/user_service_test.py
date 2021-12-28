import datetime
import unittest
from api import connection
from crm_user.user_service import UserService
from crm_user.user_exceptions import *


class UserServiceTest(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.service = UserService(connection)
        print('Setup Runnig')

    def test_perform_login_valid_creds(self):
        expected = {
            'mobile': '9663524112',
            'doj': datetime.date(year=2021, month=1, day=1),
            'role': 'user',
            'status': 1
        }
        actual = self.service.perform_login('9663524112', '12345678')

        self.assertDictEqual(expected, actual)

    def test_perform_login_invalid_creds(self):
        with self.assertRaises(UserNotFoundException):
            self.service.perform_login('9663524119', '12344678')

    def tearDown(self) -> None:
        super().tearDown()
        pass
