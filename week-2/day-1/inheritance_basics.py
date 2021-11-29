
class Abc:

    def abc(self):
        print('from abc')

    pass


class BadAgeException(Exception, Abc):

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def abc(self):
        super(BadAgeException, self).abc()
        print('from bad exception')
