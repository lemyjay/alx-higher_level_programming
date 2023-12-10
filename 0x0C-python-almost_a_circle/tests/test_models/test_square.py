#!/usr/bin/python3
"""
Unittest for the square module (Square class)
"""
import unittest
import os
from models.base import Base
from models.square import Square
from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """
    Test cases for the Square class.
    """

    def test_valid_values(self):
        """
        Test valid instantiation and values.
        """
        s = Square(5, 1, 2, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 1)

    def test_invalid_size(self):
        """
        Test case for invalid size.
        """
        with self.assertRaises(ValueError) as context:
            s = Square(-5)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_invalid_x(self):
        """
        Test case for invalid x.
        """
        with self.assertRaises(ValueError) as context:
            s = Square(5, -1)
        self.assertEqual(str(context.exception), "x must be >= 0")

    def test_valid_y(self):
        """
        Test case for valid y.
        """
        s = Square(5, 0, 0, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertEqual(s.id, 1)

    def test_valid_x_and_y(self):
        """
        Test case for valid x and y.
        """
        s = Square(5, 2, 3, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 2)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 1)

    # Add more test cases similar to the TestRectangle class

    def test_default_values(self):
        """
        Test instantiation with default values.
        """
        s = Square(5)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)
        self.assertIsNotNone(s.id)

    def test_large_values(self):
        """
        Test instantiation with large values.
        """
        s = Square(10**6, 10**6, 10**6, 1)
        self.assertEqual(s.size, 10**6)
        self.assertEqual(s.x, 10**6)
        self.assertEqual(s.y, 10**6)
        self.assertEqual(s.id, 1)

    def test_invalid_type(self):
        """
        Test case for invalid type.
        """
        with self.assertRaises(TypeError) as context:
            s = Square("5", 2, 1, 1)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_zero_values(self):
        """
        Test case for zero values.
        """
        with self.assertRaises(ValueError) as context:
            s = Square(0, 0, 0, 0)
        self.assertEqual(str(context.exception), "id must be greater than 0")

    def test_zero_values_with_valid_id(self):
        """
        Test case for zero values but with valid id
        """
        with self.assertRaises(ValueError) as context:
            s = Square(0, 0, 0, 1)
        self.assertEqual(str(context.exception), "width must be > 0")

    def test_float_values(self):
        """
        Test case for float values.
        """
        with self.assertRaises(TypeError) as context:
            s = Square(5.5, 2, 1, 1)
        self.assertEqual(str(context.exception), "width must be an integer")

    def test_valid_area(self):
        """
        Test case for calculating the area with valid values.
        """
        s = Square(5, 1, 1, 1)
        self.assertEqual(s.area(), 25)

    def test_display(self):
        """
        Test case for displaying a square.
        """
        s = Square(3, 2, 2, 1)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            s.display()
            expected_output = "\n\n  ###\n  ###\n  ###\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_with_position(self):
        """
        Test case for displaying a square with a specified position.
        """
        s = Square(4, 6, 2, 1)
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            s.display()
            expected_output = "\n\n      ####\n      ####\n"
            expected_output += "      ####\n      ####\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str_representation(self):
        """
        Test case for checking the string representation of the Square.
        """
        s = Square(4, 2, 1, 12)
        expected_output = "[Square] (12) 2/1 - 4"
        self.assertEqual(str(s), expected_output)

    def test_str_representation_large_values(self):
        """
        Test case for checking the string representation with large values.
        """
        s = Square(10**6, 10**6, 10**6, 999)
        expected_output = "[Square] (999) 1000000/1000000 - 1000000"
        self.assertEqual(str(s), expected_output)

    def test_str_representation_default_values(self):
        """
        Test case for checking the string representation with default values.
        """
        s = Square(5)
        expected_output = "[Square] ({}) 0/0 - 5".format(s.id)
        self.assertEqual(str(s), expected_output)

    def test_update_with_args(self):
        """
        Test case for updating Square attributes using *args.
        """
        s = Square(5, 5, 5, 1)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 5)

        s.update(10)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 5)

        s.update(10, 20)
        self.assertEqual(s.id, 10)
        self.assertEqual(s.size, 20)
        self.assertEqual(s.x, 5)
        self.assertEqual(s.y, 5)

        # Add more update test cases similar to TestRectangle class

    def test_update_with_kwargs(self):
        """
        Test case for updating attributes using **kwargs.
        """
        s = Square(10, 20, 30, 40)
        s.update(id=1, size=2, x=3, y=4)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_with_args_and_kwargs(self):
        """
        Test case for updating attributes using both *args and **kwargs.
        """
        s = Square(10, 20, 30, 40)
        s.update(1, 2, 3, 4, 5, id=6, size=7, x=8, y=9)
        self.assertEqual(s.id, 1)   # *args takes precedence
        self.assertEqual(s.size, 2)  # *args takes precedence
        self.assertEqual(s.x, 3)  # *args takes precedence
        self.assertEqual(s.y, 4)  # *args takes precedence

    def test_update_with_extra_args(self):
        """
        Test case for updating attributes with extra *args.
        """
        s = Square(10, 20, 30, 40)
        s.update(1, 2, 3, 4, 5, 6)  # Extra argument
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_update_with_extra_kwargs(self):
        """
        Test case for updating attributes with extra **kwargs.
        """
        s = Square(10, 20, 30, 40)
        # Extra keyword argument
        s.update(id=1, size=2, x=3, y=4, extra=5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.size, 2)
        self.assertEqual(s.x, 3)
        self.assertEqual(s.y, 4)

    def test_to_dictionary_default_values(self):
        """
        Test to_dictionary with default values.
        """
        s = Square(5)
        expected_dict = {'id': s.id, 'size': 5, 'x': 0, 'y': 0}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_to_dictionary_custom_values(self):
        """
        Test to_dictionary with custom values.
        """
        s = Square(3, 2, 1, 99)
        expected_dict = {'id': 99, 'size': 3, 'x': 2, 'y': 1}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_to_dictionary_large_values(self):
        """
        Test to_dictionary with large values.
        """
        s = Square(10**6, 10**5, 10**4, 10**3)
        expected_dict = {'id': s.id, 'size': 10**6, 'x': 10**5, 'y': 10**4}
        self.assertEqual(s.to_dictionary(), expected_dict)

    def test_to_json_string_normal_case(self):
        # Test case: Normal case with a single square
        s = Square(4, 2, 3, 7)
        dictionary = s.to_dictionary()
        json_result_normal = Base.to_json_string([dictionary])
        result = '[{{"id": {}, "size": 4, "x": 2, "y": 3}}]'.format(str(s.id))
        self.assertEqual(sorted(json_result_normal), sorted(result))

    def test_to_json_string_edge_cases(self):
        # Test case: List with multiple dictionaries
        s1 = Square(5, 2, 1, 9)
        s2 = Square(3, 0, 0, 5)
        dictionary1 = s1.to_dictionary()
        dictionary2 = s2.to_dictionary()
        json_result_multiple = Base.to_json_string([dictionary1, dictionary2])
        result = (
                '[{{"id": {}, "size": 5, "x": 2, "y": 1}}, '
                '{{"id": {}, "size": 3, "x": 0, "y": 0}}]'
                .format(str(s1.id), str(s2.id))
                )
        self.assertEqual(sorted(json_result_multiple), sorted(result))

    def test_save_to_file_normal_case(self):
        """
        Test saving a list of Square instances to a file.
        """
        s1 = Square(5, 2, 1, 9)
        s2 = Square(3, 0, 0, 5)
        Square.save_to_file([s1, s2])

        with open("Square.json", "r") as file:
            content = file.read()
            result = (
                    '[{"id": 9, "size": 5, "x": 2, "y": 1}, '
                    '{"id": 5, "size": 3, "x": 0, "y": 0}]'
                    )
            self.assertEqual(content, result)

    def test_save_to_file_empty_list(self):
        """
        Test saving an empty list to a file.
        """
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[]')

    def test_save_to_file_with_None(self):
        """
        Test saving None to a file.
        """
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[]')

    def tearDown(self):
        # Clean up created files after each test
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_from_json_string_square_normal_case(self):
        # Test case: Normal case for Square
        json_string = '[{"id": 1, "size": 5, "x": 2, "y": 3}]'
        result = Square.from_json_string(json_string)
        expected = [{'id': 1, 'size': 5, 'x': 2, 'y': 3}]
        self.assertEqual(result, expected)

    def test_from_json_string_square_empty_string(self):
        # Test case: Empty string for Square
        json_string = ""
        result = Square.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_square_none(self):
        # Test case: None input for Square
        json_string = None
        result = Square.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_create_square(self):
        """
        Test creating a Square instance using the create class method.
        """
        s1 = Square(4, 2)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertIsInstance(s2, Square)
        self.assertIsNot(s1, s2)
        self.assertEqual(s1, s2)

    def test_create_square_with_negative_size(self):
        """
        Test creating a Square instance with a negative size using the create class method.
        """
        s = Square.create(size=-5)
        self.assertIsInstance(s, Square)
        self.assertEqual(s.size, 1)  # Default size is 1


if __name__ == '__main__':
    unittest.main()
