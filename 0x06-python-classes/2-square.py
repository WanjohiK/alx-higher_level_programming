#!/usr/bin/python3
class Square:
    """ A class that defines a square

    Attributes:
        size (obj,'int'): size of the square
    """

    def __init__(self, size=0):
        """ Initializes square class

        Args:
            size (obj:'int') size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        """ Only positive integers allowed for attribute size

        """
        self.__size = size
        """ Set private attribute of square size to var size

        """
