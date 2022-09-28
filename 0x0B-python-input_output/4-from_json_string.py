#!/usr/bin/python3
'''decode in Python'''


def to_json_string(my_obj):
    '''gives the python representation of a json object
    Args:
        my_obj (obj): object
    Return: the python representation of my_obj
    '''
    import json
    return (json_loads(my_obj))
