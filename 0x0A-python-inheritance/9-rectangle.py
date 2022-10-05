#!/usr/bin/python3
'''Class Rectangle that inherits from BaseGeometry'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class Rectangle'''
    def __init__(self, width, height):
        '''Initialization
        Args:
            width (int): width of rectangle
            height (int): height og rectangle
        '''
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        '''Return the area of rectangle'''
        return (self.__width * self.__height)

    def __str__(self):
        '''How print a rectangle'''
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
