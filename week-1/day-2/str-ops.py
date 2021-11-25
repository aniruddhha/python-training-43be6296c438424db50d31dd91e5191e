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


multi_line()
