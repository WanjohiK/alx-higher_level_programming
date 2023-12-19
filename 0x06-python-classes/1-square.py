#!/usr/bin/python3
""" Square module """


class Square:

    """Define a Square class

     Attributes:
        (size,'int'): size of square
    """

    def __init__(self, size=0):
        """Initialize square class

        Args:
        (obj:'int') size of square
        """
        self.__size = size
        """
        Set size as a private attribute of square to var size
        """
