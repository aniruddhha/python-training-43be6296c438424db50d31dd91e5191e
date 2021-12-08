'''
- num should be greater than 10
- result should be greater than 10
- negative numbers are not allowed
- zeros are not allowed
- num1 should be less than num2
'''


def add(num1: int, num2: int) -> None:
    if num1 > 10 and num2 > 10:
        return num1 + num2
    return -1
