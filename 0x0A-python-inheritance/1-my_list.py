#!/usr/bin/python3
'''Module for Class MyList'''


class MyList(list):
    '''Class MyList that inherits from list'''
    def print_sorted(self):
        rtn = self.copy()
        rtn.sort()
        print(rtn)
