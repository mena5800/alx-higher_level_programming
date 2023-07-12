#!/usr/bin/python3

"""
this module contian one class Student
"""


class Student:
    """
    this class has 3 attributes and 2 function
    """

    def __init__(self, first_name, last_name, age):
        """
        initialization funcition
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        return attributes in dict
        """
        if attrs is None:
            return self.__dict__
        else:
            my_dict = {}

            for attr in attrs:
                if self.__dict__.get(attr, None) is not None:
                    my_dict[attr] = self.__dict__[attr]
            return my_dict

    def reload_from_json(self, json):
        """
        that replaces all attributes of the Student instance
        """
        for key, value in json.items():
            self.__dict__[key] = value
