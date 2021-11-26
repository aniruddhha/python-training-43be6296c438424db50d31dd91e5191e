'''
    Dictionary
    1. duplicate keys are not allowed
    2. duplicate values are allowed
'''


def basics():
    names = {
        1: 'abc',
        2: 'pqr',
        3: 'lmn',
        3: 'hhh'
    }
    print(names)

    names = dict([
        (1, 'abc'),
        (2, 'pqr'),
        (3, 'lmn'),
        (4, 'lmn')
    ])
    print(names)

    print(type(names.values()))
    print(names.values())
    print(list(names.values()))
    print([*names.values()])

    print(type(names.keys()))
    print(names.keys())
    print(set(names.keys()))
    print({*names.keys()})


basics()
