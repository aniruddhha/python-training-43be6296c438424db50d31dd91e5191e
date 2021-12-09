import unittest

from api import app, api


class MobileResourceTest(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app
        self.client = app.test_client()

    def test_for_valid_parameter(self):
        obj = ['1234567890', '7894561230']

        response = self.client.post('/mobile', json=obj)
        expected_status = 201

        self.assertEqual(response.status_code, expected_status)

    def test_for_invalid_parameter(self):
        obj = {'ab': 123}
        response = self.client.post('/mobile', json=obj)
        expected_status = 400

        self.assertEqual(response.status_code, expected_status)

    def test_for_invalid_parameter_v2(self):
        obj = ('7894561230', '1234567890')
        response = self.client.post('/mobile', json=obj)
        expected_status = 201

        self.assertEqual(response.status_code, expected_status)

    def test_invalid_mobile_number_length(self):
        obj = ('12345678900', '9876543210')
        response = self.client.post('/mobile', json=obj)
        expected_status = 400
        self.assertEqual(response.status_code, expected_status)

    def test_invalid_mobile_number_alpha(self):
        obj = ('123456789a', 'A876543210')
        response = self.client.post('/mobile', json=obj)
        expected_status = 400
        self.assertEqual(response.status_code, expected_status)

    def test_invalid_mobile_number_special_chars(self):
        obj = ('12345.67890', '4876&543210')
        response = self.client.post('/mobile', json=obj)
        expected_status = 400
        self.assertEqual(response.status_code, expected_status)

    def test_invalid_mobile_number_special_chars_v2(self):
        obj = ('1234567890', '4876$543210')
        response = self.client.post('/mobile', json=obj)
        expected_status = 400
        self.assertEqual(response.status_code, expected_status)
