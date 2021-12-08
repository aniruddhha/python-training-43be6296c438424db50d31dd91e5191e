'''
    - create a list which can contain numbers, strings and booleans
    - square each element of tuple 
    - add new element to tuple of strings
    - sort the values of dictionary by descending order
'''


class DataManipulation:

    def list_of_elements(self, *args):
        valid_types = [str, bool, int, float]

        lst = [*args]
        for itm in lst:
            if type(itm) not in valid_types:
                return None

        return lst

    def square_each_tuple(self): pass
    def add_new_element_tuple(self): pass
    def sort_dict_vals(self): pass
