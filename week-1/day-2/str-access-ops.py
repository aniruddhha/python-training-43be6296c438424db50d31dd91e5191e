def elements():
    os = 'anxroid'

    print(f'0th : {os[0]}, 2nd : {os[2]}')
    print(f'-1: {os[-1]}, -2: {os[-2]}')


def slice_it():
    os = 'android'
    print(os[1:3])
    print(os[-1:-3])
    print(os[:4])
    print(os[3:])


slice_it()
