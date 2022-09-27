#!/usr/bin/python3
'''this module open and read a file'''

def read_file(filename=""):
    '''Functionthat reads into a file
    Args:
        filename (str): name of the file
    '''
    with open(filename) as f:
            print(f.read())
