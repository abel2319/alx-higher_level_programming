#!/usr/bin/python3
'''class MyInt'''


class MyInt(int):
    '''class MyInt'''

    def __eq__(self, value):
        '''!= opeartor'''
        return (self.real != value)

    def __ne__(self, value):
        '''== operator'''
        return (self.real == value)
