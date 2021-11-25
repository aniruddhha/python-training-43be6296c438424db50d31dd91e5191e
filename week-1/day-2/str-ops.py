def basics():
    dt = 'android'
    bt = "android 't' "
    print(dt, bt)


def multi_line():
    v = 10

    dt = ''' 
        This is android with version {ver}
        with varibles will also work.
     '''.format(ver=v)

    print(dt)

    dt = f''' 
        This is android with version {v}
        with varibles will also work.
     '''

    print(dt)


def str_eqlt():
    nm = 'android'
    mm = 'androidmmm'

    assert nm == mm
    print('All Well')


def str_len():
    nm = 'android'
    print(f'Length of string is {len(nm)}')


def str_rep(n=5):
    print('android\n'*n)


str_rep(20)
