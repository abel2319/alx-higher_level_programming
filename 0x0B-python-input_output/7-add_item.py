#!/usr/bin/python3
'''This module defines a function that loads data in a json file'''
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    mylist = load_from_json_file("add_item.json")
    if len(sys.argv) > 1:
        for i in range(len(sys.argv)):
            mylist.append(sys.argv[i])
    save_to_json_file(mylist, "add_item.json")

