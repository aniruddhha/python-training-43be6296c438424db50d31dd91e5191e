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


def operations():
    names = dict([
        (1, 'abc'),
        (2, 'pqr'),
        (3, 'lmn'),
        (4, 'lmn')
    ])

    names.update([
        (6, 'gty'),
        (7, 'opl')
    ])

    names.update({
        9: 'nby',
        10: 'vft'
    })

    print(names)

    print(names.get(10))

    print(names.pop(9))
    print(names)

    items_names = list(names.items())
    print(items_names)

    for itm in items_names:
        print(itm)


operations()
