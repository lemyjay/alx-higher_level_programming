#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    This the class for testing the max_integer function using
    the unittest module
    """
    def test_regular_list(self):
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_reversed_list(self):
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer())
    
    def test_positive_numbers(self):
        result = max_integer([10, 5, 8, 3])
        self.assertEqual(result, 10)
    
    def test_negative_numbers(self):
        result = max_integer([-5, -8, -3, -1])
        self.assertEqual(result, -1)

    def test_single_numbers(self):
        self.assertEqual(max_integer([-8595]), -8595)
        self.assertEqual(max_integer([8595]), 8595)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([0, -1, -89]), 0)
        self.assertEqual(max_integer([-5, 0, 3, -1]), 3)