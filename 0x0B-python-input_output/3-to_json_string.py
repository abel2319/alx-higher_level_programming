#!/usr/bin/python3
'''encode with json'''


def to_json_string(my_obj):
    '''gives the json representation of an object
    Args:
        my_obj (obj): object
    Return: the json representation of my_obj
    '''
    import json
    return (json_dump(my_obj))
