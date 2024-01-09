#!/usr/bin/python3
"""
1-write_file Module
"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    Args:
        filename: name of file.
        test: text to be written
        Return:the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        testfile = file.write(text)
        return (testfile)
