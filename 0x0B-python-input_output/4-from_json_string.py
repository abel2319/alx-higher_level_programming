#!/usr/bin/python3
'''decode in Python'''
import json


def to_json_string(my_obj):
    '''gives the python representation of a json object
    Args:
        my_obj (obj): object
    Return: the python representation of my_obj
    '''
    return (json_loads(my_obj))
