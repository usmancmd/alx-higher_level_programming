#!/usr/bin/python3
"""inserts a line of text to a file, after each line"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file"""
    new = ""
    with open(filename, 'r', encoding="utf-8") as file_obj:
        for line in file_obj:
            new += line
            if search_string == line:
                new += new_string
    with open(filename, 'w', encoding='utf-8') as obj:
        obj.write(new)
