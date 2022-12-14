#!/usr/bin/python3
'''decode in Python'''
import json


def from_json_string(my_str):
    '''gives the python representation of a json object
    Args:
        my_obj (obj): object
    Return: the python representation of my_obj
    '''
    return (json.loads(my_str))
