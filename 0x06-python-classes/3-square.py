#!/usr/bin/python3
"""Create class Square that defines a square"""


class Square:

    """class Square that defines a square"""

    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of the square
        """

        # instance attribute/variable
        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

    # instance method
    def area(self):
        """Returns area of a square"""

        return self.__size * self.__size
