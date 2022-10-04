#!/usr/bin/python3
'''Class Rectangle that inherits from BaseGeometry'''


class Rectangle(7-base_geometry.BaseGeometry):
    '''Class Rectangle'''
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.width = width
        self.height = height
