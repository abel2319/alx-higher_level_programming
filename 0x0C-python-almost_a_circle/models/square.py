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

    @property
    def size(self):
        """method that return the size of the square
        """
        return (self.width)

    @size.setter
    def size(self, value):
        """mtehod that retrieve the size of the square
        Args:
            value (int): the new value of size
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        '''update all attribute of an instance
        Args:
            args (list): the list of arguments
            kwargs (dict): the dict of arguemnts
        '''
        if args and len(args) > 0:
            if len(args) == 1:
                self.id = args[0]

            elif len(args) == 2:
                self.id = args[0]
                self.size = args[1]

            elif len(args) == 3:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]

            elif len(args) == 4:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]

        elif kwargs:
            for arg, val in kwargs.items():
                if arg == "id":
                    self.id = val
                elif arg == "size":
                    self.size = val
                elif arg == "x":
                    self.x = val
                elif arg == "y":
                    self.y = val
