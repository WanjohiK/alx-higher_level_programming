#!/usr/bin/python3
"""
6-base_geometry Module
"""


class BaseGeometry:
    """A class with public attribute area"""
    def area(self):
        """raises an exception if not called"""
        raise Exception("area() is not implemented")
