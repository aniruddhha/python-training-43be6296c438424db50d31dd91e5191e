import unittest
from data_structures import DataManipulation
import datetime


class DataStrsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.dm = DataManipulation()

    def test_is_list(self):

        lst = self.dm.list_of_elements(True, False, True)
        self.assertIsInstance(lst, list)

    def test_check_valid_types_bool(self):
        lst = self.dm.list_of_elements(True, False, True)
        self.assertIsNotNone(lst)

    def test_check_valid_types_int(self):
        lst = self.dm.list_of_elements(1, 2, 3)
        self.assertIsNotNone(lst)
        self.assertIsInstance(lst, list)

    def test_check_invalid_types(self):
        lst = self.dm.list_of_elements(
            datetime.date(2021, 2, 12),
            False,
            True,
            'abc',
            12.3,
            45
        )
        self.assertIsNone(lst)

    def test_mix_types(self):
        lst = self.dm.list_of_elements(
            False,
            True,
            'abc',
            12.3,
            45
        )
        self.assertIsNotNone(lst)
        self.assertIsInstance(lst, list)

    def tearDown(self) -> None:
        self.dm = None
