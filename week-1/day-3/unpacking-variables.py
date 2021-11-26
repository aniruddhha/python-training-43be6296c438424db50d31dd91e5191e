
def sample_runner(start, stop, step):
    for i in range(start, stop, step):
        print(i)


def sample_display(ver, os, is_stock):
    print(f'Version : {ver}, OS : {os}, Stock : {is_stock}')


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

    lp_dtl = (1, 10, 2)
    sample_runner(lp_dtl[0], lp_dtl[1], lp_dtl[2])
    sample_runner(*lp_dtl)

    # print(type(names))
    # print(type(*names))


def unpacking_dictionary():
    names = {'ver': 10, 'os': 'android', 'is_stock': True}
    sample_display(names.get('ver'), names.get('os'), names.get('is_stock'))
    sample_display(**names)


unpacking_dictionary()
