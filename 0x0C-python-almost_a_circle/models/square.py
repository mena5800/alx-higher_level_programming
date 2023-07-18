#!/usr/bin/python3

"""
this module contain Square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    module square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        init function
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        function return info about the square
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width,)

    @property
    def size(self):
        """
        getter size
        """
        return self.height

    @size.setter
    def size(self, val):
        """
        setter size
        """
        self.width = val
        self.height = val

    def to_dictionary(self):
        """
        returns the dictionary representation of a Square:
        """
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
