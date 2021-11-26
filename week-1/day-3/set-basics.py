def basics():
    lst = ['abc', 'pqr', 'lmn', 'abc']

    names = {'abc', 'pqr', 'lmn', 'abc'}
    print(names)

    names = set(lst)
    print(names)
    # names[2] = 'nnn'
    # print(names)

    # print(names[1:3])


def operations():
    st1 = {'a', 'b'}
    st2 = {'b', 'd'}

    print('--- Minus ---')
    print(st1 - st2)

    print('---Union---')
    print(st1.union(st2))

    print('---Intersection---')
    print(st1.intersection(st2))

    print('---Difference---')
    print(st1.difference(st2))

    print('--- Are Disjoint ---')
    print(st1.isdisjoint(st2))


basics()
