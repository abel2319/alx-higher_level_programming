#!/usr/bin/python3
'''This module allows the addition of two integers or flaots'''


def add_integer(a, b=98):
    '''this funstion add two intergers or floats

        Return the sum of a and b

        Exceptions:
            raise TypeError if a and/or b are not integers or floats
    '''
    if (type(a) is not int) and (type(a) is not float):
        raise TypeError("a must be an integer")
    if (type(b) is not int) and (type(b) is not float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
