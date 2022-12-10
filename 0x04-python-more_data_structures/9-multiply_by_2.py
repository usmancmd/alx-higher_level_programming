#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    copy = a_dictionary.copy()
    new_list = list(copy.keys())
    for k in new_list:
        copy[k] = copy[k] * 2
    return copy
