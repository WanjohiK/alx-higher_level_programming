#!/usr/bin/python3
"""
square Module
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        initialize method
        arributes:
            size:size of square
            x: x coordinate
            y: y coordinate
            id: square object
        """
        super().__init__(size, size,  x, y, id)

    def __str__(self):
        """print method
        return:
            string representation of square
        """
        return ("[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                              self.id, self.x,
                                              self.y, self.width))

    @property
    def size(self):
        """ width getter method
            return:
                width and height size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        width setter method
        args:
            value: size of value
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update square method
        args:
            args: pointer to arguments
            kwargs: double pointer to key word arguments
        """

        if args:
            i = 0
            updated = ['id', 'size', 'x', 'y']
            for arg in args:
                setattr(self, updated[i], arg)
                i += 1
            return
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary representation of Square
        return:
            dictionary
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}
