def elements():
    os = 'anxroid'

    print(f'0th : {os[0]}, 2nd : {os[2]}')
    print(f'-1: {os[-1]}, -2: {os[-2]}')


def slice_it():
    os = 'android'

    print('0', os[0])  # a
    print('1', os[1])  # n
    print('2', os[2])  # d
    print('3', os[3])  # r
    print('4', os[4])  # o
    print('5', os[5])  # i
    print('6', os[6])  # d

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
    print('[-1:]', os[:-1])

    # 0 = a, 1 = n , 2 = d, 3 = r, 4 = o, 5 = i, 6 = d

    # a = -7 , n = -6 , d = -5 , r = -4 , o = -3 , i = -2 , d = -1

    print('[0:4:1]', os[0:4:1])
    print('[0:4:2]', os[0:5:2])
    print('[::-1]', os[::-1])


