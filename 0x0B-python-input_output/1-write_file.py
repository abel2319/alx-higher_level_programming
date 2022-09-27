#!/usr/bin/python3
'''Module that overwrite in a file'''


def write_file(filename="", text=""):
    '''overwrite a string at the end of a text file (UTF8)
    Args:
        filename (str): the name of file
        text (str): the string
    '''
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)
