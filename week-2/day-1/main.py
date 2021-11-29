from car import Car, Abc
# import car


def classes_and_objejcts():
    cr = Car()  # object cr is called ORV
    cr.speed = 20
    cr.light = 30
    cr.print_car()

    cr.speed_up()
    cr.turn_on_light()
    cr.turn_off_light()

    self = 10
    print(self)

    cr1 = Car()
    cr2 = Car()
    cr3 = Car()
    cr4 = Car()

    cr1.speed = 55
    cr1.light = 56
    cr1.print_car()

    cr1.turn_off_light()

    abc = Abc()  # object


if __name__ == '__main__':
    classes_and_objejcts()
