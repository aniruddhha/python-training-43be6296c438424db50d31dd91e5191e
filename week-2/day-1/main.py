from datetime import date
from car import Car, Abc
from builtin_classes import AgeCalculator, Employee
# import car


def classes_and_objejcts():
    cr = Car()  # object cr is called ORV
    cr.speed = 20
    cr.light = 30
    cr.print_car()
    print(id(cr))

    cr.speed_up()
    cr.turn_on_light()
    cr.turn_off_light()

    self = 10
    print(self)

    cr1 = Car()
    print(id(cr1))

    cr2 = Car()
    cr3 = Car()
    cr4 = Car()

    cr1.speed = 55
    cr1.light = 56
    cr1.print_car()

    cr1.turn_off_light()

    abc = Abc()  # object


def classes_obj_constructor():
    ob1 = Abc(10, 20, 30)


def age():
    ac = AgeCalculator()
    print(
        ac.calculate_age(
            date(1555, 11, 20)
        )
    )


def emp():
    e = Employee('abc', 35)
    e.info()


if __name__ == '__main__':
    emp()
