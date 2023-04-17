#!/usr/bin/python3
"""Module containing the rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Class represention of a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the Rectangle class attributes
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            Returns width attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Sets width attribute
        """
        self.type_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """
            Returns height attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Sets height attribute
        """
        self.type_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """
            Returns x attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            Sets x attribute
        """
        self.type_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """
            Returns y attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            Sets y attribute
        """
        self.type_validator("y", value)
        self.__y = value

    def area(self):
        """
            Returns the area of the rectangle
        """
        return self.height * self.width

    def display(self):
        """
            Prints the representation of the rectangle to stdout
        """
        print(("\n" * self.__y) +
              "\n".join(((" " * self.__x) + ("#" * self.__width))
                        for i in range(self.__height)))

    def update(self, *args, **kwargs):
        """
            Updates the class arguments
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                setattr(self, key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            Returns a dictionary representation the class
        """
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'height': self.height,
                'width': self.width}

    def __str__(self):
        """
            Overwritting the str method
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)


if __name__ == "__main__":

    r1 = Rectangle(10, 2)
    print(r1.id)

    r2 = Rectangle(2, 10)
    print(r2.id)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
