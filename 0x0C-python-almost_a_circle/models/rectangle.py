#!/usr/bin/python3

"""
this module contian class Rectangle
"""
from base import Base


class Rectangle(Base):
    """
    this Rectangle class inherit from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        initialization method
        """
        super().__init__(id)

        self.__validate_int_positive(width, "width")
        self.__width = width

        self.__validate_int_positive(height, "height")
        self.__height = height

        self.__validate_int_positive(x, "x")
        self.__x = x

        self.__validate_int_positive(y, "y")
        self.__y = y

    def __validate_int_positive(self, value, property):
        """
        function to check if value is int and positive otherwise
        raise error
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(property))

        if property in ["width", "height"]:
            if value <= 0:
                raise ValueError("{} must be > 0".format(property))

        if property in ["x", "y"]:
            if value < 0:
                raise ValueError("{} must be >= 0".format(property))

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        width setter
        """
        self.__validate_int_positive(width, "width")
        self.__width = width

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        height setter
        """
        self.__validate_int_positive(height, "height")
        self.__height = height

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        x setter
        """
        self.__validate_int_positive(x, "x")
        self.__x = x

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        y setter
        """
        self.__validate_int_positive(y, "y")
        self.__y = y

    def area(self):
        """
        return the area of rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        prints in stdout the Rectangle instance with the character
        # - you don't need to handle x and y here.
        """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """
        Update the class Rectangle by overriding the __str__ method so that it returns
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
    
    def update(self, *args):
        """
        Update the class Rectangle by adding the public method def update(self, *args):
        that assigns an argument to each attribute:
        """        
        self.id = args[0]
        self.__width = args[1]
        self.__height = args[2]
        self.__x = args[3]
        self.__y = args[4]