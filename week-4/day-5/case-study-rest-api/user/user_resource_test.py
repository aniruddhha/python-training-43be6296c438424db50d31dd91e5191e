
from api import app

import unittest


class UserResourceTest(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app
        self.client = app.test_client()

    def test_post_user_valid(self):
        user = {
            'user_id': 15,
            'user_name': 'mxcviuertyieuryt',
            'password': '123456789',
            'role': 'admin'
        }

        expected = {
            'sts': 'success',
            'msg': 'user created successfully',
            'res': 1
        }
        response = self.client.post('/user', json=user)
        actual = response.get_json()
        self.assertDictEqual(expected, actual)
