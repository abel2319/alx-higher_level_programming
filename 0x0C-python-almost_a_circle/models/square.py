#!/usr/bin/python3
'''Module that defines the class square'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Class Square that enherits from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initialization
        Args:
            size (int): size of the square
            x (int): absciss
            y (int): ordonate
            id (int): id
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''Representation of a square'''
        return ("[square] ({}) {}/{} - {}".format(self.id,
                                                  self.x,
                                                  self.y,
                                                  self.width))
