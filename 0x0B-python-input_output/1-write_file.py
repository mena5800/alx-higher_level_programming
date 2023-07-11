#!/usr/bin/python3

"""
this module contain only one function write_file
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file and returns the number of characters written

    Arguments:
                filename: the name of file
                text: the text to write in file
    """
    num_char = 0
    with open(filename, mode='w', encoding="utf-8") as f:
        num_char = f.write(text)

    return num_char
