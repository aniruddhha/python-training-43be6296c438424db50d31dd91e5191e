
from db.config import *

import json


# this function returns jsonabale version of given object

def con_obj(ofgdfgjdgk):
    print(ofgdfgjdgk)
    return vars(ofgdfgjdgk)


cfg = Config()

# cfg object converted to dictionary
# cfg_dict = vars(cfg)

print(json.dumps(cfg, default=con_obj))

print(json.dumps(cfg, default=lambda o: vars(o)))

js_str = json.dumps(cfg, default=lambda o: vars(o))

# conevert all nested objects to the dictionary


lst = ['abc', 'pqr']
print(json.dumps(lst))

dct = {'dt': 'allow', 'age': 45, 'sts': True}
print(json.dumps(dct))

tpl = (67, 89, 90, None)
print(json.dumps(tpl))


print()
