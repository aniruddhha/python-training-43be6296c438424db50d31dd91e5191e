

def basic_while():
    cnt = 0
    while cnt < 3:
        cnt += 1
        print(cnt)


def while_with_list():
    data = ['abc', 'pqr', 'lmn']
    cnt = 0
    while cnt < len(data):
        print(data[cnt])
        cnt += 1
