class Car:
    def __init__(self) -> None:
        self.speed = 10

    def speed_up(self):
        self.speed += 10
        return 100

    def go_to_speed(self, speed):
        self.speed = speed * 2
        return self.speed
