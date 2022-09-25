#!/usr/bin/python3
'''This module defines a class rectangle'''


class Rectangle:
    '''class Rectangle
    '''

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """init method to define object's attributes
        Args:
            size (int): size of the square
        """

        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

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

    def area(self):
        """method that return the area of the rectangle
        """
        return (self.__height * self.__width)

    def perimeter(self):
        """method that returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__height + self.__width))

    def __rep__(self):
        """method that returns a string representation of the rectangle
        """
        string = f"Rectangle({self.__width}, {self.__height})"
        return (string)

    def __str__(self):
        """method that returns a string representation of the rectangle
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for j in range(0, self.__height):
            for i in range(0, self.__width):
                string += '#'
            string += '\n'
        return (string)

    def __del__(self):
        """method that delete an instance of the class
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
