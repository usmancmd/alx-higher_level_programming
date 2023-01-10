#!/usr/bin/python3
"""writes to a text file"""


def write_file(filename="", text=""):
    with open(filename, mode="w", encoding="utf-8") as file_obj:
        return file_obj.write(text)
