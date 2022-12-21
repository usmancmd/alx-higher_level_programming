#!/usr/bin/python3
"""Create class Square that defines a square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size):
        """initialize square
        Args:
            size (int): size of the square
        """

        # instance attribute
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        if type(self.__size) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return self.__size * self.__size
