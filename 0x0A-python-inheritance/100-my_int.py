#!/usr/bin/python3
"""class MyInt that inherits from int"""


class MyInt(int):
    """class MyInt"""
    def __eq__(self, other):
        return int(str(self)) != other

    def __ne__(self, other):
        return int(str(self)) == other
