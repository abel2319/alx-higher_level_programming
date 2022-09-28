#!/usr/bin/python3
'''This module defines a function that loads data in a json file'''

def load_from_json_file(filename):
    '''load data in a json file
    '''
    import json
    with open(filename, encoding="utf-8") as file:
        return (json.load(file))
