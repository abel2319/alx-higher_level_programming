#!/usr/bin/python3
'''Module for Class MyList'''


class MyList(list):
    '''Class MyList that inherits from list'''
    def __init__(self):
        '''Initialization'''
        super().__init__()

    def print_sorted(self):
        '''Return the list sorted'''
        rtn = sorted(self)
        print(rtn)
