#!/usr/bin/python3

"""
this module has only one function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Write a function that inserts a line of text to a file, after each
    line containing a specific string (see example):
    """
    with open(filename, encoding="utf-8")as f:
        lines = f.readlines()

    for i in range(len(lines)):
        if search_string in lines[i]:
            lines.insert(i+1, new_string)

    with open(filename, encoding="utf-8", mode='w') as f:
        f.writelines(lines)
