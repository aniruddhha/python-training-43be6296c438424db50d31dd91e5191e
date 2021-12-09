'''
    - consider that this pg class has been given to you by Payment Gateway provider
    - we are simulating that this object is somehow not available in testing environment, so we are mocking it

'''


class Pg:

    def transfer(self, amt):
        return 1

    def deposit(self, amt):
        return 2

    def withdraw(self, amt):
        return 3

    def balance(self, account):
        return 323
