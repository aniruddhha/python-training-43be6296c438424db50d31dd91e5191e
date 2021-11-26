def unpacking_sequence():
    names = ['abc', 'pqr', 'lmn']
    print(names)
    print(*names)

    names = ('abc', 'pqr', 'lmn')
    print(names)
    print(*names)

    names = {'abc', 'pqr', 'lmn'}
    print(names)
    print(*names)

    # print(type(names))
    # print(type(*names))


unpacking_sequence()
