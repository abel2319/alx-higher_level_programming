#!/usr/bin/python3
'''class square'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''class Square that inherits from Rectangle'''
    def __init__(self, size):
        '''initialization
        Args:
            size (int): size of a side
        '''
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

