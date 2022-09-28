#!/usr/bin/python3
'''decode in Python'''
import json


def class_to_json(obj):
    '''gives the python representation of a json object
    Args:
        obj (obj): object
    Return: the json representation of obj
    '''
    return (json.dumps(obj.__dict__))
