#!/usr/bin/python3

"""
this module contian class Rectangle
"""
from models.base import Base


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
        for i in range(self.__y):
            print("")

        for i in range(self.__height):
            my_str = " " * self.__x + "#" * self.__width
            print(my_str)

    def __str__(self):
        """
        Update the class Rectangle by overriding the __str__ method so that it
        returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.__x, self.__y,
                                                       self.__width,
                                                       self.__height)

    def update(self, *args, **kwargs):
        """
        Update the class Rectangle by adding the public method
        def update(self, *args):that assigns an argument to each attribute:
        """
        my_attributes = ["id", "_Rectangle__width",
                         "_Rectangle__height",
                         "_Rectangle__x", "_Rectangle__y"]
        for i in range(len(args)):
            self.__validate_int_positive(args[i], my_attributes[i])
            self.__dict__[my_attributes[i]] = args[i]

        if len(args) == 0:
            for key, value in kwargs.items():
                self.__validate_int_positive(value, key)
                self.__dict__["_Rectangle__{}".format(key)] = value

    def to_dictionary(self):
        """
        returns the dictionary representation of a Rectangle:
        """
        return {"id": self.id, "width": self.width,
                "height": self.height,
                "x": self.x, "y": self.y}
