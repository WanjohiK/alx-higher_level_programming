#!/usr/bin/python3
class Square:
    """ A class that defines a square

    Attributes:
        size (obj: 'int'): size of the square
        area (obj: 'int'): area of the square
    """

    def __init__(self, size=0):
        """ Initializes square class

        Args:
            size (obj:'int'): for size attribute
        """
        self.__size = size
        """ Set private attribute of square size to var size

        """

    @property
    def size(self):
        """ Defines size of square object

        """
        return self.__size

    def area(self):
        """ Defines area of square object

        """
        return self.__size ** 2

    @size.setter
    def size(self, value):
        """ Defines size of square object to change to value

        Args:
            size (obj:'int') size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        """ Only positive integers allowed for attribute size

        """
        self.__size = value
