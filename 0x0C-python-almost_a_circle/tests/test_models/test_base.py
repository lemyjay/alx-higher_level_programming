#!/usr/bin/python3
"""
Unittest for the base module (Base class)
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class.
    """

    def test_constructor_with_id(self):
        """
        Test constructor when providing a positive integer id.
        """
        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_constructor_without_id(self):
        """
        Test constructor when not providing an id.
        """
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_constructor_with_negative_id(self):
        """
        Test constructor with a negative id.
        """
        with self.assertRaises(ValueError) as context:
            Base(-5)
        self.assertEqual(str(context.exception), "id must be greater than 0")

    def test_constructor_with_float_id(self):
        """
        Test constructor with a float id.
        """
        with self.assertRaises(TypeError) as context:
            Base(3.14)
        self.assertEqual(str(context.exception), "id must be an integer")

    def test_constructor_with_string_id(self):
        """
        Test constructor with a string id.
        """
        with self.assertRaises(TypeError) as context:
            Base("abc")
        self.assertEqual(str(context.exception), "id must be an integer")

    def test_constructor_with_list_id(self):
        """
        Test constructor with a list id.
        """
        with self.assertRaises(TypeError) as context:
            Base([1, 2, 3])
        self.assertEqual(str(context.exception), "id must be an integer")

    def test_constructor_with_dict_id(self):
        """
        Test constructor with a dict id.
        """
        with self.assertRaises(TypeError) as context:
            Base({"key": "value"})
        self.assertEqual(str(context.exception), "id must be an integer")

    def test_constructor_with_boolean_id(self):
        """
        Test constructor with a boolean id.
        """
        with self.assertRaises(TypeError) as context:
            Base(True)
        self.assertEqual(str(context.exception), "id must be an integer")


if __name__ == '__main__':
    unittest.main()
