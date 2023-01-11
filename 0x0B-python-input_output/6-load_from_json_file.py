#!/usr/bin/python3
"""creates an Object"""
import json


def load_from_json_file(filename):
    """creates an Object from a "JSON file"""
    with open(filename, 'r', encoding='utf-8') as file_obj:
        return json.load(file_obj)
