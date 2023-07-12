#!/usr/bin/python3

"""
this module contain script that adds all arguments
to a Python list, and then save them to a file:


"""
import json
import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

arguments = sys.argv

# remove first elemnt the name of file
arguments.pop(0)

try:
    elements = load_from_json_file("add_item.json")
    elements.extend(arguments)
    save_to_json_file(elements, "add_item.json")
except Exception as e:
    save_to_json_file(arguments, "add_item.json")
