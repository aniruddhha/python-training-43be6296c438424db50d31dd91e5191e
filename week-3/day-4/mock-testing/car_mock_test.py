from unittest.mock import Mock


car = Mock()

car.speed_up()
car.speed_up.assert_called()
car.speed_up.assert_called_once()
car.speed_up()
car.speed_up.assert_called_once()
