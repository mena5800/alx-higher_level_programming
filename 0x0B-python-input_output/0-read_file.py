#!usr/bin/python3

"""
this module contain only one function read_file
"""


def read_file(filename=""):
    """
    function that reads a text file (UTF8) and prints it to stdout:

    Arguments:
                filename: the name of file
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        print(f.read())
