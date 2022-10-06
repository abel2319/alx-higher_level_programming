#!/usr/bin/python3
''''''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''''''
    def __init__(self, size, x=0, y=0, id=None):
        '''Initialization
        Args:
            size (int): size of the square
            x (int): absciss
            y (int): ordonate
            id (int): id
        '''
        super().__init__(self, size, size, x, y, id)

    def __str__(self):
        ''''''
        return ("[square] ({}) {}/{} - {}".foramt(self.id,
                                                  self.__x,
                                                  self.__y,
                                                  self.__size))
