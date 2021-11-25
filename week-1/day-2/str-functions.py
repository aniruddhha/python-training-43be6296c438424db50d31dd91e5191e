def str_funs():
    os = '         android     '
    print(f'os - {len(os)}')
    print(f'stripped os - {len(os.strip())}')

    os = 'android is good operating system'
    print(os.title())
    print(os.capitalize())
    print(os.upper())
    print(os.find('is'))
    print(os.count('i'))
    print(os.replace('good', 'best'))

    os = '123bbb'
    print('is digit : ', os.isdigit())
    print('is alphabate : ', os.isalpha())


# ip = abc
# n = 1
# op = aBc
def caps_nth(n, st_dt):
    print('[:n]', st_dt[:n].lower())
    print('[n:]', st_dt[n:].capitalize())

    return st_dt[:n].lower() + st_dt[n:].capitalize()


print(caps_nth(2, 'abc'))
