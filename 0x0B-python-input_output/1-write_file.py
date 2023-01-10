#!/usr/bin/python3
"""writes to a text file"""


def write_file(filename="", text=""):
    """writes to a text file"""
    with open(filename, mode="w", encoding="utf-8") as file_obj:
        out = file_obj.write(text)
    return out
