def elements():
    os = 'anxroid'

    print(f'0th : {os[0]}, 2nd : {os[2]}')
    print(f'-1: {os[-1]}, -2: {os[-2]}')


def slice_it():
    os = 'android'
    print('-1', os[-1])  # d
    print('-2', os[-2])  # i
    print('-3', os[-3])  # o
    print('-4', os[-4])  # r
    print('-5', os[-5])  # d
    print('-6', os[-6])  # n
    print('-7', os[-7])  # a

    print('[1:3]', os[1:3])
    print('[-3:-1]', os[-3:-1])
    print('[:4]', os[:4])
    print('[3:]', os[3:])


slice_it()
