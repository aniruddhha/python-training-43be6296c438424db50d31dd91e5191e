from abc import abstractclassmethod
import unittest
import datetime
from unittest.case import expectedFailure
from date_util.date_to_json import *


class DateToJson(unittest.TestCase):

    def test_valid_date(self):
        inp = datetime.date(2021, 1, 1)
        expected = '2021-01-01'

        actual = date_to_string(inp)
        self.assertEqual(expected, actual)

    def test_wrong_input_obj(self):
        inp = '2021-01-01'
        expected = None

        actual = date_to_string(inp)
        self.assertEqual(expected, actual)

    def test_valid_dict_contains_date(self):
        inp = {
            'dt': datetime.date(2021, 1, 1),
            'nm': 'android',
            'ver': 12
        }

        expected = {
            'dt': '2021-01-01',
            'nm': 'android',
            'ver': 12
        }

        actual = convert_object_to_dict_which_contains_date(inp)

        self.assertDictEqual(expected, actual)
