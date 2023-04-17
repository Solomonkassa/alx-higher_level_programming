#!/usr/bin/python3
"""Module containing the square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class represention of a square
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            Returns the size
        """
        return self.width

    @size.setter
    def size(self, val):
        """
            Setting both height and width
        """
        self.type_validator("width", val)
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """
            Updates the arguments in the class
        """

        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            Returns dictionary representation the class
        """
        return {'id': self.id,
                'x': self.x,
                'size': self.size,
                'y': self.y}

    def __str__(self):
        """
            String representation of a class
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
