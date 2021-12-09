
import datetime
from invalid_date_exception import InvalidDateException


def is_date_less_than_today(dt: str):

    try:
        date_obj = datetime.date.fromisoformat(dt)
        today = datetime.date.today()
        if date_obj >= today:
            raise InvalidDateException('Date Should Be Less Than Today')

    except ValueError:
        raise

    except InvalidDateException:
        raise
