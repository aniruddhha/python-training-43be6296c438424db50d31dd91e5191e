'''
- num should be greater than 10
- result should be greater than 10
- negative numbers are not allowed
- zeros are not allowed
- num1 should be less than num2
'''


def add(num1: int, num2: int) -> None:

    if(num1 == 0 and num2 == 0):
        return -4
    if num1 > 10 and num2 > 10 and num1 < num2:
        res = num1 + num2
        if(res < 10):
            return -3
        else:
            return res
    return -1
