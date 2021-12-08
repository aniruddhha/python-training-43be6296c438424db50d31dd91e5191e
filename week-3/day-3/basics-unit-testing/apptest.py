import unittest
from app import add


class TestAddition(unittest.TestCase):

    def num_should_be_greater_than_ten(self):
        num1 = 10
        num2 = 10
        res = add(num1, num2)
        self.assertEquals(res, -1)


if __name__ == '__main__':
    unittest.main()
