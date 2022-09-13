#!/usr/bin/python3
"""A module that define a class square
"""
class Square:
    """Class that define a square
    """
    __size = 0
    
    def __init__(self, size = 0):
        """init method to define object's attributes
        Args:
            size (int): size of the square
        """
        try:
            if type(size) is not int:
                raise TypeError
            if size < 0:
                raise ValueError
            self.__size = size
        except ValueError:
            print("size must be >= 0")
        except TypeError:
            print("size must be an integer")
