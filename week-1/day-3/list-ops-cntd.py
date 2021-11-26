
data = ['hi']


def add(dt) -> None:
    data.append(dt)


def remove(dt) -> None:
    data.remove(dt)


def update(n, dt) -> None:
    data.insert(n, dt)


def display() -> None:
    print(data)


def displayNth(n) -> None:
    print(data[n])


add(10)
display()
add(20)
display()
update(1, 30)
display()
remove(10)
display()
