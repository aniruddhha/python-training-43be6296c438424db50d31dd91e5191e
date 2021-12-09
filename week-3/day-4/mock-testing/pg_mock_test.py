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
# mck_pg.balance.assert_called_with(145)

print(f'Balance Arguments {mck_pg.balance.call_args}')
print(f'Balance Count {mck_pg.balance.call_count}')
print('---Method Calls On Mock Object---')
print(mck_pg.method_calls)

mck_pg.balance.return_value = 455
dt = mck_pg.balance(133)
# if condition is true then and only then, interpreter will pass to next line
assert dt == 455
print('Yes balance returned 455')
