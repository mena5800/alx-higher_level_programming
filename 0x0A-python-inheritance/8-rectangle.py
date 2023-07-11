#!/usr/bin/python3
"""
this module class Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    class Rectangle inherit from BaseGeometry
    """

    def __init__(self, width, height):
        """
        initialization function
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
