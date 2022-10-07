#!/usr/bin/python3
'''Module that defines the base'''
import json


class Base:
    '''class Base
    Args:
        nb_objects (int): number of instances created
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialization
        Args:
            id (int): the id of the new instance
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of list_dictionaries'''
        if list_dictionaries is None:
            return ("[]")
        return (json.dumps(list_dictionaries))
