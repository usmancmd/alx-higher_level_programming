#!/usr/bin/python3
def no_c(my_string):
    copy = my_string[:]
    new = [i for i in copy if i != 'c' and i != 'C']
    return "".join(new)
