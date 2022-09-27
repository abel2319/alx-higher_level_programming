#!/usr/bin/python3
'''this module open and read a file'''


def read_file(filename=""):
    '''Functionthat reads into a file
    Args:
        filename (str): name of the file
    '''
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
