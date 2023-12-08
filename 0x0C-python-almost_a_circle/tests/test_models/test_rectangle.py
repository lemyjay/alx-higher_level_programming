#!/usr/bin/python3
"""
Unittest for the rectangle module (Rectangle class)
"""
# File: tests/test_models/test_rectangle.py
import unittest
from models.rectangle import Rectangle
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    """
    Test cases for the Rectangle class.
    """

    def test_valid_values(self):
        """
        Test valid instantiation and values.
        """
        r = Rectangle(10, 2, 1, 1, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 1)

    def test_invalid_width(self):
        """
        Test case for invalid width.
        """
        with self.assertRaises(ValueError) as context:
            r = Rectangle(-10, 2)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_invalid_height(self):
        """
        Test case for invalid height.
        """
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, -2)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_invalid_x(self):
        """
        Test case for invalid x.
        """
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2, -1)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_invalid_y(self):
        """
        Test case for invalid y.
        """
        with self.assertRaises(ValueError) as context:
            r = Rectangle(10, 2, 1, -1)
        self.assertEqual(str(context.exception), "y must be >= 0")

    def test_invalid_type(self):
        """
        Test case for invalid type.
        """
        with self.assertRaises(TypeError) as context:
            r = Rectangle("10", 2)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_default_values(self):
        """
        Test instantiation with default values.
        """
        r = Rectangle(5, 5)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

    def test_zero_values(self):
        """
        Test instantiation with zero values.
        """
        with self.assertRaises(ValueError) as context:
            r = Rectangle(0, 0, 0, 0)
        self.assertEqual(str(context.exception), "width must be > 0")

        with self.assertRaises(ValueError) as context:
            r = Rectangle(1, 0, 0, 0)
        self.assertEqual(str(context.exception), "height must be > 0")

    def test_float_width(self):
        """
        Test case for width with float value.
        """
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5.5, 10)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_float_height(self):
        """
        Test case for height with float value.
        """
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10.5)
        self.assertEqual(str(context.exception), "height must be an integer")

    def test_float_x(self):
        """
        Test case for x with float value.
        """
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2.5)
        self.assertEqual(str(context.exception), "x must be an integer")

    def test_float_y(self):
        """
        Test case for y with float value.
        """
        with self.assertRaises(TypeError) as context:
            r = Rectangle(5, 10, 2, 7.5)
        self.assertEqual(str(context.exception), "y must be an integer")

    def test_large_values(self):
        """
        Test instantiation with large values.
        """
        r = Rectangle(10**6, 10**6, 10**6, 10**6)
        self.assertEqual(r.width, 10**6)
        self.assertEqual(r.height, 10**6)
        self.assertEqual(r.x, 10**6)
        self.assertEqual(r.y, 10**6)

    def test_valid_area(self):
        """
        Test case for calculating the area with valid values.
        """
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

    def test_large_area(self):
        """
        Test case for calculating the area with large values.
        """
        r = Rectangle(10**6, 10**6)
        self.assertEqual(r.area(), 10**12)

    def test_display(self):
        """
        Test case for displaying a rectangle.
        """
        r = Rectangle(4, 6)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            r.display()
            expected_output = "####\n####\n####\n####\n####\n####\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_small_rectangle(self):
        """
        Test case for displaying a small rectangle.
        """
        r = Rectangle(2, 2)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            r.display()
            expected_output = "##\n##\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_with_position(self):
        """
        Test case for displaying a rectangle with a specified position.
        """
        r = Rectangle(4, 6, 2, 3)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            r.display()
            expected_output = "\n\n\n  ####\n  ####\n  ####\n  "
            expected_output += "####\n  ####\n  ####\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_representation(self):
        """
        Test case for checking the string representation of the Rectangle.
        """
        r = Rectangle(4, 6, 2, 1, 12)
        expected_output = "[Rectangle] (12) 2/1 - 4/6"
        self.assertEqual(str(r), expected_output)

    def test_str_representation_default_values(self):
        """
        Test case for checking the string representation with default values.
        """
        r = Rectangle(5, 5)
        expected_output = "[Rectangle] ({}) 0/0 - 5/5".format(r.id)
        self.assertEqual(str(r), expected_output)

    def test_str_representation_large_values(self):
        """
        Test case for checking the string representation with large values.
        """
        r = Rectangle(10**6, 10**6, 10**6, 10**6, 999)
        expected_output = "[Rectangle] (999) 1000000/1000000 - 1000000/1000000"
        self.assertEqual(str(r), expected_output)

    def test_update(self):
        """
        Test case for updating Rectangle attributes with *args.
        """
        r = Rectangle(5, 5, 5, 5, 1)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)

        r.update(10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)

        r.update(10, 20)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 5)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)

        r.update(10, 20, 30)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 5)

        r.update(10, 20, 30, 40)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 5)

        r.update(10, 20, 30, 40, 50)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.width, 20)
        self.assertEqual(r.height, 30)
        self.assertEqual(r.x, 40)
        self.assertEqual(r.y, 50)


if __name__ == '__main__':
    unittest.main()
