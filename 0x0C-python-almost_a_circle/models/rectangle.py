#!/bin/python3
"""Defines Rectangle class"""

class Rectangle(Base):
	"""Rectangle class"""
	def __init__(self, width, height, x=0, y=0, id=None):
		super()__init__(id)
		self.__width = width
		self.__height = height
		self.__x = x
		self.__y = y

	@property
	def width(self):
		"""Setter for the width attribute"""
		return self.__width

	@width.setter
	def width(self, value):
		pass

	@property
    def height(self):
        """Setter for the width attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        pass

	@property
    def x(self):
        """Setter for the width attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        pass

	@property
    def y(self):
        """Setter for the width attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        pass
