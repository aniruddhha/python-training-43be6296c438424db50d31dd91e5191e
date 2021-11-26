
def sample_runner(start, stop, step):
    for i in range(start, stop, step):
        print(i)


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

    lp_dtl = {1, 10, 2}
    sample_runner(*lp_dtl)

    # print(type(names))
    # print(type(*names))


def unpacking_dictionary():
    pass


unpacking_sequence()
