#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list

    i = len(my_list)
    if idx > i - 1:
        return my_list

    #cp1 = [i for i in my_list]
    #cp1[idx] = element
    #return cp1
    new_list = my_list[:]
    for i in new_list:
        if new_list[idx] == i:
            new_list = element
        return new_list
