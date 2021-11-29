class Abc:
    pass


class Car:

    speed = 20  # state
    light = 0   # state
    self = 10
    # is = 10
    # in = 10

    def speed_up(self):  # behaviour
        self.speed = 10

    def turn_on_light(self):  # behaviour
        self.light = 100

    def turn_off_light(self):  # behaviour
        self.light = 0

    def print_car(self):
        print(f' Speed {self.speed}, Light {self.light}')
