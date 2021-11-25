''' Higher Order Functions '''


def dt_fn():
    print('this is abc')


def prm_fn(xlkkjgdfkljgkldfjhlfkjgjk):  # 1. functions can be passed as parameters
    xlkkjgdfkljgkldfjhlfkjgjk()


def ret_fn():  # 2. functions can be returned from another functions
    dbb = dt_fn
    return dbb


fn = dt_fn  # 3. functions can be assigned to variables

# function can be passed as parameter
prm_fn(fn)
prm_fn(dt_fn)

# function returns another function
fn = ret_fn()
print(fn)
# fn()
