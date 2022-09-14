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
