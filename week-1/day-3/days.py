def give_me_day() -> dict:

    days = {
        1: 'mon',
        2: 'tue',
        3: 'wed',
        4: 'thu',
        5: 'fri',
        6: 'sat',
        7: 'sun'
    }

    return days


def give_me_holidays() -> set:
    return {2, 6, 8}


print(f'what is my name ? {__name__}')

if __name__ == '__main__':

    import sys

    print('--- command line arguments are ---')
    print(sys.argv)
    give_me_day()