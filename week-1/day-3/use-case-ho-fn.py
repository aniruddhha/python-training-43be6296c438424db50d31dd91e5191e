
def error_handler(err):
    print(f'Error is {err}')


def add_nums(num1, num2, hndlr):
    if(num1 > 50):
        hndlr('Num1 is greater than upper bound')


add_nums(80, 20, error_handler)
