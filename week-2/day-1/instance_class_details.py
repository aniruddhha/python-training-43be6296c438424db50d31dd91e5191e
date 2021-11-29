class InstDtls:

    cls_prop = 'cls'  # class variable

    def __init__(self, inst_prop) -> None:
        self.inst_prop = inst_prop  # instance variable

    def inst_def(self): pass

    def cls_def(self): pass


class Empty:
    def __init__(self, a) -> None:
        self._a = a  # using __ is not making any variable private, it is just a name alteration
