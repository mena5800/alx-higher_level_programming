#!/usr/bin/python3

"""
this module to class Rectangle
"""


class Rectangle:
    """
    Rectangle class
    """

    def __init__(self, width=0, height=0):
        """
        init function to initialize object
        """
        self.__is_int_pos(width, "width")
        self.__is_int_pos(height, "height")
        self.__width = width
        self.__height = height

    def __is_int(self, object):
        """
        private method to check if object int or not

        Arguments:
                        object : unknown type
        Return:
                        True if object is int or False if object is not int.
        """
        if type(object) is int:
            return True
        else:
            return False

    def __is_pos(self, num):
        """
        private method to check if num is positive or not

        Arguments:
                        num : int

                Return:
                        True is num is positive or False if num is negative
        """
        if num >= 0:
            return True
        else:
            return False

    def __is_int_pos(self, num, name):
        """
        private method to check if num is positive and positive or not.

        Arguments:
                        num : int

                Return:
                        Return True or raise exception
        """
        if self.__is_int(num) is False:
            error = name + " must be an integer"
            raise TypeError(error)

        if self.__is_pos(num) is False:
            error = name + " must be >= 0"
            raise ValueError(error)

        return True

    @property
    def width(self):
        """
        getter function to get the value of width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter function to set the value of width
        """
        self.__is_int_pos(value, "width")
        self.__width = value

    @property
    def height(self):
        """
        getter function to get the value of height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter function to set the value of height.
        """
        self.__is_int_pos(value, "height")
        self.__height = value

    def area(self):
        """
        function to return the area of Rectangle.
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        function to return the perimeter of Rectangle.
        """
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """
        function to return the shape of rectangle
        """
        shape = ""
        for i in range(self.__height):
            shape += "#" * self.__width
            if (i < self.__height - 1):
                shape += "\n"

        return shape

    def __repr__(self):
        """
        return a string representation of the rectangle to
        be able to recreate a new instance.
        """
        text = "Rectangle({},{})".format(self.__width, self.__height)
        return text

    def __del__(self):
        """
        print massage bye
        """
        print("Bye rectangle...")
