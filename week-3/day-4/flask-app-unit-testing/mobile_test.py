import unittest

from flask.wrappers import JSONMixin
from api import app, api


class MobileResourceTest(unittest.TestCase):

    def setUp(self) -> None:
        self.app = app
        self.client = app.test_client()

    def test_type_of_parameter(self):
        obj = ['1234567890', '12345678630']

        self.client.post('/mobile', json=obj)
