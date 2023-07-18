#!/usr/bin/python3

"""
this module contain class Base
"""

import json


class Base:
    """
    class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        initialization function
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries:
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file:
        """
        if list_objs is None or len(list_objs) == 0:
            with open("{}.json".format(cls.__name__), 'w') as f:
                f.write(json.dumps([]))

        else:
            with open("{}.json".format(cls.__name__), "w") as f:
                f.write(cls.to_json_string(list_objs))
