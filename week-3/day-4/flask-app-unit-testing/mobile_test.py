import unittest

from api import app, api


class MobileResourceTest(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app
        self.client = app.test_client()

    def test_for_valid_parameter(self):
        obj = ['1234567890', '12345678630']

        response = self.client.post('/mobile', json=obj)
        expected_status = 201

        self.assertEqual(response.status_code, expected_status)

    def test_for_invalid_parameter(self):
        obj = {'ab': 123}
        response = self.client.post('/mobile', json=obj)
        expected_status = 400

        self.assertEqual(response.status_code, expected_status)

    def test_for_invalid_parameter_v2(self):
        obj = (12333333, 566666)
        response = self.client.post('/mobile', json=obj)
        expected_status = 201

        self.assertEqual(response.status_code, expected_status)
