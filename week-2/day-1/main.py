from datetime import date
from car import Car, Abc
from builtin_classes import AgeCalculator, Employee
from instance_class_details import InstDtls
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


def cls_inst_dtls():
    dtl1 = InstDtls('inst1')

    dtl2 = InstDtls('inst2')

    dtl3 = InstDtls('inst3')

    print('Before Setting CLS')
    print(dtl1.cls_prop, ',', dtl2.cls_prop, ',', dtl3.cls_prop)
    print('After Setting CLS')

    dtl1.cls_prop = 'cls1'
    InstDtls.cls_prop = 'cls1'

    print(dtl1.cls_prop, ',', dtl2.cls_prop, ',', dtl3.cls_prop)
    print('----------------------------')
    print('Before Setting INST')
    print(dtl1.inst_prop, ',', dtl2.inst_prop, ',', dtl3.inst_prop)
    print('After Setting INST')
    dtl1.inst_prop = 'inst11'
    print(dtl1.inst_prop, ',', dtl2.inst_prop, ',', dtl3.inst_prop)


if __name__ == '__main__':
    cls_inst_dtls()
