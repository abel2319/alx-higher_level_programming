#!/usr/bin/python3
'''This module defines a function that loads data in a json file'''
import json


def load_from_json_file(filename):
    '''load data in a json file
    '''
    with open(filename, encoding="utf-8") as file:
        return (json.loads(file))
