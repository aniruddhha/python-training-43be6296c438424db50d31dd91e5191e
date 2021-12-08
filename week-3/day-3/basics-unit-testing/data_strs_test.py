import unittest
from data_structures import DataManipulation


class DataStrsTest(unittest.TestCase):

    def test_is_list(self):
        dm = DataManipulation()
        lst = dm.list_of_elements(True, False, True)
        self.assertIsInstance(lst, list)
