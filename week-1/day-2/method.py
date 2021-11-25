''' Methods/Functions and its definations '''


def info():
    print('hellow')


def info_details():
    print('here are machine details')


def info_with_parameter(isSql, con):
    print('Is SQL Db : ', isSql)
    print('Connection : ', con)


def info_with_return():
    print('well I am returning')
    return 20


info()
info_details()
info_with_parameter(False, "http://abc.com")

ret = info_with_return()
print('Return Value is ', ret)
