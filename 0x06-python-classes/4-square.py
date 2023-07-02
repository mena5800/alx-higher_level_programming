#!/usr/bin/python3

"""
this module has class Square
"""


class Square:
    """
    class Square

    attributes:
                size
    """

    def __init__(self, size=0):
        """
        constructor of class Square

        arguments:
                        size : the size of class
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        get the area of square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        retrieve the value of size
        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        set the value of private attribute size
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
