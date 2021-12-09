import unittest
from api import app, api


class HelloResourceTest(unittest.TestCase):
    def setUp(self) -> None:
        self.app = app
        self.client = app.test_client()

    def test_hello_available(self):
        response = self.client.get('/hello')
        self.assertIsNotNone(response)

    def test_hello_get(self):
        response = self.client.get('/hello')
        expected = {
            'os': 'android',
            'version': '11',
            'name':  'not-named'
        }
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.get_json(), expected)

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
