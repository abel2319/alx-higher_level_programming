#!/usr/bin/python3

"""A module that define a class square
"""


class Square:
    """Class that define a square
    """
    __size = 0

    def __init__(self, size=0):
        """init method to define object's attributes
        Args:
            size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """method that return the area of the square
        """
        return (self.__size * self.__size)
    
    @property
    def size(self):
        """mtehod that retrieve the size of the square
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """method to set a new size
        Args:
            value (int): new size of the square
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints in stdout the square with the character #:
                if size is equal to 0, prints an empty line
        """
        if self.__size != 0:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
