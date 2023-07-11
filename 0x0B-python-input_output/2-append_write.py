#!usr/bin/python3

"""
this module contain only one function append_write
"""


def append_write(filename="", text=""):
    """
        appends a string at the end of a text file and returns
        the number of characters added.
    Arguments:
                filename: the name of file
                text: the text to write in file
    """
    num_char = 0
    with open(filename, mode='a', encoding="utf-8") as f:
        num_char = f.write(text)

    return num_char
