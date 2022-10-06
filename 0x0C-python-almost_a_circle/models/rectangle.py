#!/usr/bin/python3
from base import Base


class Rectangle(Base):
    '''class Rectangle that inherits from base
    '''

    def __init__(self, width, height, x=0, y=0, id=None): 
        """init method to define object's attributes
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
            x (int): x
            y (int): y
            id (int): id
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """method that return the width of the square
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """mtehod that retrieve the width of the square
        Args:
            value (int): the new value of width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """method that return the height of the square
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """mtehod that retrieve the height of the square
        Args:
            value (int): the new value of height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """method that return the width of the square
        """
        return (self.__x)

    @width.setter
    def x(self, value):
        """mtehod that retrieve the width of the square
        Args:
            value (int): the new value of width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__x = value
    
    @property
    def y(self):
        """method that return the width of the square
        """
        return (self.__y)

    @y.setter
    def width(self, value):
        """mtehod that retrieve the width of the square
        Args:
            value (int): the new value of width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__y = value
