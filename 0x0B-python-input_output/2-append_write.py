#!/usr/bin/python3
"""
2-append_write Module
"""


def append_write(filename="", text=""):
    """
    appends a string at the end of a text file
    Args:
        filename: name of file
        text: text to append
    Return:the number of characters added
    """
    with open(filename, "a", encoding="utf-") as file:
        textfile = file.write(text)
        return textfile
