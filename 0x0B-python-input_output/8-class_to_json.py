#!/usr/bin/python3
'''endecode in Python'''
import json


def class_to_json(obj):
    '''gives the python representation of a python object
    Args:
        obj (obj): object
    Return: the json representation of obj
    '''
    return (json.dumps(obj.__dict__))
