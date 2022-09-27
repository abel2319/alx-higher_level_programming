#!/usr/bin/python3
'''Module to append in a file'''


def append_write(filename="", text=""):
    '''appends a string at the end of a text file (UTF8)
    Args:
        filename (str): the name of file
        text (str): text to append
    Return: the number of characters added
    '''
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)
        return (len(text))
