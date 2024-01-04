#!/usr/bin/python3
""" Rectangle module """


class Rectangle:

    """
    Declare a rectangle class
    """
    number_of_instances = 0
    print_symbol = "#"

    @classmethod
    def square(cls, size=0):
        """
        returns a new Rectangle instance that is a square
        with width == height == size
        """
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    def __init__(self, width=0, height=0):
        """initialize class by setting attributes
        height and width
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __del__(self):
        """
        prints a string when an instance has been destroyed
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """
        getter for the private instance attribute width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the private instance attribute width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        getter for the private instance attribute height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the private instance attribute height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        returns the area of the rectangle
        """
        return self.height * self.width

    def perimeter(self):
        """
        returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.height * 2) + (self.width * 2)

    def __str__(self):
        """
        returns printable string rep of the rectangle
        """
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join(str(self.print_symbol) * self.__width
                                for i in range(self.__height))
        return string

    def __repr__(self):
        """
        Return the string representation of the rectangle
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
