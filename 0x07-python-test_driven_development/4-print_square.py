#!/usr/bin/python3
'''This module is used to print a square with #'''


def print_square(size):
    '''This function prints a square with the character #

    exceptions:
        TypeError
        ValueError

    Args:
        size (int): size of the square
    '''
    if type(size) is not int:
        raise TypeError("size msut be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end='')
        print("")
