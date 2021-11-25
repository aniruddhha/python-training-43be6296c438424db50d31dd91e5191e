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


str_funs()
