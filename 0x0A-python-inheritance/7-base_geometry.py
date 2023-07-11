#!/usr/bin/python3#!/usr/bin/python3
"""
module has class BaseGeometry
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
        if type(value) != int:
            error_message = "{} must be an integer".format(name)
            raise TypeError(error_message)

        if value <= 0:
            error_message = "{} must be greater than 0".format(name)
            raise ValueError(error_message)
