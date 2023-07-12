#!/usr/bin/python3

"""
this module contain function load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    writes an Object to a text file, using a JSON representation
    """
    with open(filename, encoding="utf-8") as f:
        return json.loads(f.read())
