#!/usr/bin/python3
'''This module is used to print two strings'''


def say_my_name(first_name, last_name=""):
    '''This function print the first and last name

    exceptions:
        TypeError

    Args:
        first_name (str): first name
        last_name (str): last name
    '''
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
