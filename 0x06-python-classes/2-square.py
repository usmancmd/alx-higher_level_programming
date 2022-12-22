#!/usr/bin/python3

"""Create class Square that defines a square"""


class Square:
    """class Square that defines a square"""
    def __init__(self, size=0):
        """initialize square
        Args:
            size (int): size of the square
        """
        self.__size = size  # size of the square
        if type(size) is not int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
