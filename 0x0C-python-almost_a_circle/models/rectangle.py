#!/usr/bin/python3
'''Module for class Rectangle'''
from models.base import Base


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
        super().__init__(id)
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
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """method that return the x of the square
        """
        return (self.__x)

    @x.setter
    def x(self, value):
        """method that retrieve the x of the square
        Args:
            value (int): the new value of x
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """method that return the y of the rectangle
        """
        return (self.__y)

    @y.setter
    def y(self, value):
        """method that retrieve the y of the rectangle
        Args:
            value (int): the new value of y
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method that return the area of the rectangle
        """
        return (self.__height * self.__width)

    def display(self):
        """method that prints a string representation of the rectangle
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return ("")
        for i in range(0, self.__y):
            string += '\n'
        for j in range(0, self.__height):
            for i in range(0, self.__x):
                string += ' '
            for i in range(0, self.__width):
                string += "#"
            if j < (self.__height - 1):
                string += '\n'
        print(string)

    def __str__(self):
        """method that returns a string representation of the rectangle
        """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                        self.x,
                                                        self.y,
                                                        self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        '''update all attribute of an instance
        Args:
            args (list): the list of arguments
        '''
        if args and len(args) > 0:
            if len(args) == 1:
                self.id = args[0]

            elif len(args) == 2:
                self.id = args[0]
                self.width = args[1]

            elif len(args) == 3:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]

            elif len(args) == 4:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]

            elif len(args) == 5:
                self.id = args[0]
                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]

        elif kwargs:
            for arg, val in kwargs.items():
                if arg == "id":
                    self.id = val
                elif arg == "width":
                    self.width = val
                elif arg == "height":
                    self.height = val
                elif arg == "x":
                    self.x = val
                elif arg == "y":
                    self.y = val
