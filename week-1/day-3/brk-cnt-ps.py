
def break_demo():
    for i in range(10):
        if(i > 8):
            break


def continue_demo():
    for i in range(10):
        if (i < 5) and (i > 3):
            continue
        else:
            break


def pass_demo(): pass


break_demo()
continue_demo()
pass_demo()
