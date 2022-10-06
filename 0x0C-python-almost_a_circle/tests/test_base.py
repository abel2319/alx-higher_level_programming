#!/usr/bin/python3
"""Unittest
"""
import os
import unittest
from models.base import Base

class TestBase_instantiation(unittest.TestCase):
    """Testing instantiation of the Base class."""

    def test_no_arg(self):
        a = Base()
        b = Base()
        self.assertEqual(a.id, 4)
        self.assertEqual(b.id, a.id + 1)

    def test_None_id(self):
        b = Base(None)
        self.assertEqual(b.id, 1)

    def test_unique_id(self):
        a = Base(5)
        self.assertEqual(5, a.id)

    def test_autoencrement_after_instance_with_an_given_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_id_public(self):
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_nb_instances_private(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_float_id(self):
        self.assertEqual(5.5, Base(5.5).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == "__main__":
    unittest.main()
