from unittest.mock import MagicMock
from car import Car

cr: Car = Car()

cr.speed_up = MagicMock(abc=2)
cr.speed_up()
