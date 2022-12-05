#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        cp = my_list.copy()
        return cp

    i = len(my_list)
    if idx > i - 1:
        return cp

    cp = my_list[:]
    cp[idx] = element
    return cp
