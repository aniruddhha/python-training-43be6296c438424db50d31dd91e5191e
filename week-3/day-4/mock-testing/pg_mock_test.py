from unittest.mock import Mock
from pg import Pg

pg = Pg()
print(pg.transfer(122))
print(pg.balance(123))
# some how this Pg object is not availabe in test environment
# in such cases you need to fake or mock the Pg object
# and here you mocking framework will come into the picture

print('--- Mocking begins here --- ')
mck_pg = Mock()  # fake object
mck_pg.balance(133)
mck_pg.transfer(455)
mck_pg.deposit(410)
mck_pg.withdraw(500)


# mck_pg.balance(133)
mck_pg.balance.assert_called()
mck_pg.balance.assert_called_once()
mck_pg.balance.assert_called_with(133)
mck_pg.balance.assert_called_with(145)
