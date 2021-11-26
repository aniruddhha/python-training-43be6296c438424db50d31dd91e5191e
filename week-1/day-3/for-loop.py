def basic_for():
    names = ['abc', 'pqr', 'lmn']

    for n in range(5):
        print(n)

    for name in names:
        print(name, end=',')


def nested_for():
    for i in range(3):
        print(f'-- {i} --')
        for j in range(3):
            print(j, ' ')


nested_for()
