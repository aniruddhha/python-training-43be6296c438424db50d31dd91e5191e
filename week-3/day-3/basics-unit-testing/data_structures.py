'''
    - create a list which can contain numbers, strings and booleans
    - square each element of tuple 
    - add new element to tuple of strings
    - sort the values of dictionary by descending order
'''


class DataManipulation:

    def tpl_elm_checker(el):
        if(type(el) == int or type(el) == float):
            return el ** 2
        return None

    def list_of_elements(self, *args):
        valid_types = [str, bool, int, float]

        lst = [*args]
        for itm in lst:
            if type(itm) not in valid_types:
                return None

        return lst

    def square_each_tuple_element(self, *args):
        lst = [*args]
        return tuple(map(self.tpl_elm_checker, lst))

    def add_new_element_tuple(self): pass

    def sort_dict_vals(self, dt: dict):
        if(type(dt) != dict):
            return None
        lst = [*dt.values()]
        sorted(lst, reverse=True)
