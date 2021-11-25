def list_elements() -> None:
    days = [2, 6, 5, 7, 9, 10, 23, 45]
    print(days[2:4:1])
    print(days[6])
    print(days[1:6:2])


def list_elements_index() -> None:
    days = ['sun', 'mon', 'tue', 'wed']
    print(f"Index of sun is {days.index('mon')}")


list_elements_index()
