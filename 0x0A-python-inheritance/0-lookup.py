#!/usr/bin/python3
'''This module define a function that returns the list of
available attributes and methods of an object:'''


def lookup(obj):
    '''This function returns  the list of available attributes
    and methods of an object'''
    return (dir(obj))
