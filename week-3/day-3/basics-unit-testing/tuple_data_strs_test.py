import unittest
from data_structures import DataManipulation


class TupleDataStrsTest(unittest.TestCase):

    def setUp(self) -> None:
        self.dm = DataManipulation()

    def test_check_data_type_tuple(self):
        tpl = self.dm.square_each_tuple_element(12, 30, 12)
        self.assertIsInstance(tpl, tuple)

    def test_element_square_valid(self):
        tpl = self.dm.square_each_tuple_element(2, 3, 2)
        expected = (4, 9, 4)
        self.assertTupleEqual(tpl, expected)

    def test_element_square_invalid(self):
        tpl = self.dm.square_each_tuple_element(2, 3, 2)
        wrong_expcted = (4, 10, 4)
        self.assertNotEqual(tpl, wrong_expcted)

    def test_element_square_negative(self):
        tpl = self.dm.square_each_tuple_element(2, 3, -2)
        expcted = (4, 9, 4)
        self.assertTupleEqual(tpl, expcted)
