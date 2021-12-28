import datetime
import json


def date_to_string(dt):
    if isinstance(dt, (datetime.date, datetime.datetime)):
        return dt.isoformat()


def convert_object_to_dict_which_contains_date(raw_obj):
    json_str = json.dumps(
        raw_obj,
        default=date_to_string
    )
    converted_json_dict = json.loads(json_str)
    return converted_json_dict
