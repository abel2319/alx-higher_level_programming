#!/usr/bin/python3
"""Unittest class Rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_creation(unittest.TestCase):
    '''Testing instantiation of class Rectangle
    '''

    def test_inheritance_from_base(self):
        self.assertIsInstance(Rectangle(0, 0), Base)


if __name__ == "__main__":
    unittest.main()
