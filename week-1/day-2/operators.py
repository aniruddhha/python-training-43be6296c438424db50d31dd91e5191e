''' Operators in python '''

num1 = 10
num2 = 20


def arithmatic():
    print('Addition is : ', num1 + num2)
    print('Subtraction is : ', num1 - num2)
    print('Multiplication is : ', num1 * num2)
    print('Division is : ', num1 / num2)
    print('Exponent : ', num1 ** 2)
    print('Floor Division : ', num1 // 2)
    print('Modulas : ', num1 % 2)


def assignment():
    ver = 10
    print('Version : ', ver)
    a, b = 10, 20
    a, b = 50, ver
    a += 10
    a -= b
    a *= 20
    a = a - b
    a = a * 20
    print('a, b', a, b)


def bitwise():
    a = 10
    b = 20
    print('And : ', a & b)
    print('Or : ', a | b)
    print('Xor : ', a ^ b)
    print('Not : ', ~a)

    a &= b
    print('And = :', a)


def comparision():
    print(' Equality ', num1 == num2)
    print(' Greater Than ', num1 > num2)
    print(' Less Than ', num1 < num2)
    print(' Greater Equals', num1 >= num2)
    print(' Not Equals', num1 != num2)


comparision()
