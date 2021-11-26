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


'''
A list comprehension consists of brackets containing an expression followed by a for clause,
then zero or more for or if clauses. The result will be a new list resulting from evaluating
the expression in the context of the for and if clauses which follow it.
'''


def list_for_demo():
    names = ['abc', 'pqr', 'lmn']
    print(names)

    names = [name.upper() for name in names]
    print(names)


list_for_demo()
