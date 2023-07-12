#!/usr/bin/python3

"""
this module contain function save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    with open(filename, encoding="utf-8", mode="w") as f:
        f.write(json.dumps(my_obj))
