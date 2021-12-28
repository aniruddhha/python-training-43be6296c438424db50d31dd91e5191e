import datetime
import unittest
from api import app
from crm_user.user_service import UserService
from crm_user.user_exceptions import *


class UserManipulationResourceTest(unittest.TestCase):

    def setUp(self) -> None:
        self.client = app.test_client()

    def test_login_with_valid_creds(self):

        req_obj = {
            'user_name': '9663524112',
            'password': '12345678'
        }

        expcted_response = {
            'sts': 'success',
            'msg': 'user logged in successfully',
            'res': {
                'mobile': '9663524112',
                'doj': '2021-01-01',
                'role': 'user',
                'status': 1
            }
        }

        raw_response = self.client.post('/user/login', json=req_obj)
        actual_response = raw_response.get_json()

        self.assertDictEqual(expcted_response, actual_response)

    def test_login_with_invalid_creds(self):
        req_obj = {
            'user_name': '9663524118',
            'password': '12345679'
        }
        expcted_response = {
            'sts': 'fail',
            'msg': 'You are entering wrong credentials',
            'res': 'user not found'
        }

        raw_response = self.client.post('/user/login', json=req_obj)
        actual_response = raw_response.get_json()

        self.assertDictEqual(expcted_response, actual_response)
