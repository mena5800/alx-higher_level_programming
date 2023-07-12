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

    def to_json(self):
        """
        return attributes in dict
        """
        return self.__dict__
