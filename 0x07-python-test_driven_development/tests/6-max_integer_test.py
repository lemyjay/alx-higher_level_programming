#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase)
    """
    This the class for testing the max_integer function using
    the unittest module
    """
    def test_empty(self):
        self.assertEqual(max_integer(), None)
    
    def test_max(self):
        self.assertEqual([1, 2, 3, 4], 4)
        self.assertEqual([-8595], -8595)
        self.assertEqual([0, -1, -89], 0)

    def test_elements(self):
        self.assertRaises (TypeError, ["s", 5, 6])

