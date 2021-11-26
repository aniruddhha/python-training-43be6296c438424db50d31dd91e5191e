'''
    Set Observations
    1. unoredered and unindexed
    2. non subscriptable
    3. elemennts can be added 
    4. sequences can be added
    5. elemnets can be removed
    6. set operations can performed
    7. duplicates are not allowed
'''


def basics():
    lst = ['abc', 'pqr', 'lmn', 'abc']

    names = {'abc', 'pqr', 'lmn', 'abc'}
    print(names)

    names = set(lst)
    print(names)
    names.add('bbb')
    names.update(['kkk', 'vvv'])
    names.remove('bbb')

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
