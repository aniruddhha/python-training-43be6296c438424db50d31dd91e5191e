''' Methods/Functions and its definations '''


def info():
    print('hellow')


def info_details():
    print('here are machine details')


def info_with_parameter(isSql=True, con='default'):
    print('Is SQL Db : ', isSql)
    print('Connection : ', con)


def info_with_return():
    print('well I am returning')
    return 20


# info()
# info_details()
info_with_parameter(
    False,
    'http://abc.com'
)

info_with_parameter(
    con='http://pqr.com',
    isSql=True
)

info_with_parameter()

# ret = info_with_return()
# print('Return Value is ', ret)
