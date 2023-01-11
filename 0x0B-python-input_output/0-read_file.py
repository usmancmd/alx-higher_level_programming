#!/usr/bin/python3
"""Reads a file and print to stdout"""


def read_file(filename=""):
    """reads a text file"""
    with open(filename, encoding='utf-8') as file_obj:
        print(file_obj.read(), end="")
