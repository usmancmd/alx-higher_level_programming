#!/usr/bin/python3
"""appends a string at the end of a file"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file"""
    with open(filename, mode='a', encoding='utf-8') as file_obj:
        return file_obj.write(text)
