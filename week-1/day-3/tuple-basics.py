'''
    Tupple Observations
    1. ordered
    2. duplicates allowed
    3. immutable
'''


def basics():
    names = ('abc', 'pqr', 'lmn', 'abc', 'pqr')
    print(names)

    names = tuple(['abc', 'pqr', 'lmn'])
    print(names)

    # names[2] = 'jjj'

    print(names.index('pqr'))
    print(names.count('abc'))


basics()
