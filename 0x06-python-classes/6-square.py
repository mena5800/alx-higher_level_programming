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

    def __init__(self, size=0, position=(0, 0)):
        """
        constructor of class Square

        arguments:
            size: the size of class
            position: the position of square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """
        prints in stdout the square with the character #:
        """
        if self.__size == 0:
            print()

        for i in range(self.__size):
            print("_" * self.__position[0], "#" * self.__size, sep='')

    @property
    def position(self):
        return self.__position

    @position.getter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
