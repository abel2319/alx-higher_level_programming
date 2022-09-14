#!/usr/bin/python3

"""A module that define a class square
"""


class Square:
    """Class that define a square
    """
    __size = 0

    def __init__(self, size):
        """init method to define object's attributes
        Args:
            size (int): size of the square
        """
        self.__size = size
