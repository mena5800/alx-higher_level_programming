#!/usr/bin/python3
"""
this module class Rectangle
"""


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """
        fucntion to raise error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        function to check that value is int and > 0
        """
        if type(value) is not int:
            error_message = "{} must be an integer".format(name)
            raise TypeError(error_message)

        if value <= 0:
            error_message = "{} must be greater than 0".format(name)
            raise ValueError(error_message)


class Rectangle(BaseGeometry):
    """
    class Rectangle inherit from BaseGeometry
    """

    def __init__(self, width, height):
        """
        initialization function
        """
        self.__width = width
        self.__height = height

        self.integer_validator("width", width)
        self.integer_validator("height", height)
