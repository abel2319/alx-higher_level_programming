#!/usr/bin/python3
'''This module defines a class rectangle'''


class Rectangle:
    '''class Rectangle
    '''

    def __init__(self, width=0, height=0):
        """init method to define object's attributes
        Args:
            size (int): size of the square
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """method that return the width of the square
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """mtehod that retrieve the width of the square
        """
        if type(value) is not int:
            raise TypeError("width mest be an integer")
        if value < 0:
            raise ValueError("width mest be >= 0")
        self.__width = value

    @property
    def height(self):
        """method that return the height of the square
        """
        return (self.__width)

    @height.setter
    def height(self, value):
        """mtehod that retrieve the height of the square
        """
        if type(value) is not int:
            raise TypeError("height mest be an integer")
        if value < 0:
            raise ValueError("height mest be >= 0")
        self.__height = value
