#!/usr/bin/python3
'''This module defines a function that saves data in a json file'''
import json


def save_to_json_file(my_obj, filename):
    '''save data in a json file
    '''
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, f)
