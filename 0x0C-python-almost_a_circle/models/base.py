#!/usr/bin/python3
"""Defines  base class"""
import json


class Base:
    """Defines  base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dicts"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        with open(filename, "w") as jsfile:
            if list_objs is None:
                jsfile.write("[]")
            else:
                for obj in list_objs:
                    list_dicts = obj.to_dictionary()
                jsonfile.write(Base.to_json_string(list_dicts))
