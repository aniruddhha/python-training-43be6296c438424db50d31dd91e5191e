def calculate(num1, num2, n):
    names = [10, 20, 30]

    try:
        res = num1/num2 + names[n]

    except ZeroDivisionError:
        res = 0

    except IndexError:
        res = -1

    return res


def calculate_with_n(num1, num2, n):
    names = [10, 20, 30]

    try:
        res = num1/num2 + names[n]  # python adds raise statement

    except (ZeroDivisionError, IndexError):
        res = 0

    return res


def list_prop(n):
    names = [10, 20, 30]
    print(names[n])


print(f'Result is {calculate(10, 20, 1)}')
print(f'Result is {calculate(50, 96, 0)}')
print(f'Result is {calculate(1, 1, 0)}')
print(f'Result is {calculate(1, 0, 1)}')
print(f'Result is {calculate(0, 1, 10)}')
print('welcome to python')

# list_prop(1)
# list_prop(10)
