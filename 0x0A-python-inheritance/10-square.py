#!/usr/bin/python3

"""
this module contian class square
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    this class contain only one function init
    """

    def __init__(self, size):
        """
        initialization function
        """
        self.__size = size
        super().__init__(size, size)
        self.integer_validator("size", size)

    def area(self):
        """
        fucntion return the area of square
        """
        return self.__size * self.__size
