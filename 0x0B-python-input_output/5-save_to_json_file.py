#!/usr/bin/python3
"""function that writes an Object to a text file, using a JSON"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file"""
    with open(filename, 'w', encoding='utf-8') as file_obj:
        json.dump(my_obj, file_obj)
