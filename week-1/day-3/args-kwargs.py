def normal_args(*name):
    print(type(name))
    print(name)


def kw_args(**name):
    print(type(name))
    print(name)


def normal_kw_args(*args, **kwargs):
    print(args)
    print(kwargs)


normal_args('abc', 'pqr', 'lmn', 'xyz')
kw_args(con='abc', lskffjldkfjgldfkgj=10, is_live=False)

normal_kw_args('abc', 'pqr', con='bbb', ver=78)
normal_kw_args(con='bbb', sver=78)
