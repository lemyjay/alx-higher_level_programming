#!/usr/bin/python3
"""
Unittest for the rectangle module (Rectangle class)
"""
# File: tests/test_models/test_rectangle.py
import unittest
import os
import json
from models.base import Base
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

    def test_init_with_extra_args(self):
        """
        Test case for initializing a Rectangle with extra arguments.
        """
        err_msg = "__init__() takes from 3 to 6 positional arguments"
        err_msg += " but 7 were given"
        with self.assertRaises(TypeError) as context:
            r = Rectangle(10, 20, 30, 40, 50, 60)  # Extra argument
        self.assertEqual(str(context.exception), err_msg)

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

    def test_update_with_args(self):
        """
        Test case for updating Rectangle attributes using *args.
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

        r1 = Rectangle(10, 20, 30, 40, 50)
        r1.update(1, 2, 3, 4, 5)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)

    def test_update_with_kwargs(self):
        """
        Test case for updating attributes using **kwargs.
        """
        r = Rectangle(10, 20, 30, 40, 50)
        r.update(id=1, width=2, height=3, x=4, y=5)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_with_args_and_kwargs(self):
        """
        Test case for updating attributes using both *args and **kwargs.
        """
        r = Rectangle(10, 20, 30, 40, 50)
        r.update(1, 2, 3, 4, 5, id=6, width=7, height=8, x=9, y=10)
        self.assertEqual(r.id, 1)   # *args takes precedence
        self.assertEqual(r.width, 2)  # *args takes precedence
        self.assertEqual(r.height, 3)  # *args takes precedence
        self.assertEqual(r.x, 4)  # *args takes precedence
        self.assertEqual(r.y, 5)  # *args takes precedence

    def test_update_with_extra_args(self):
        """
        Test case for updating attributes with extra *args.
        """
        r = Rectangle(10, 20, 30, 40, 50)
        r.update(1, 2, 3, 4, 5, 6)  # Extra argument
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_with_extra_kwargs(self):
        """
        Test case for updating attributes with extra **kwargs.
        """
        r = Rectangle(10, 20, 30, 40, 50)
        # Extra keyword argument
        r.update(id=1, width=2, height=3, x=4, y=5, extra=6)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_to_dictionary_default_values(self):
        """
        Test case for to_dictionary with default values.
        """
        r = Rectangle(5, 5)
        expected_dict = {'id': r.id, 'width': 5, 'height': 5, 'x': 0, 'y': 0}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_dictionary_non_default_values(self):
        """
        Test case for to_dictionary with non-default values.
        """
        r = Rectangle(10, 8, 2, 4, 7)
        expected_dict = {'id': 7, 'width': 10, 'height': 8, 'x': 2, 'y': 4}
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_dictionary_large_values(self):
        """
        Test case for to_dictionary with large values.
        """
        r = Rectangle(10**6, 10**6, 10**6, 10**6, 999)
        expected_dict = {
                'id': 999, 'width': 10**6,
                'height': 10**6, 'x': 10**6,
                'y': 10**6
                }
        self.assertEqual(r.to_dictionary(), expected_dict)

    def test_to_json_string(self):
        # Test case: Non-empty list of dictionaries
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_result = Base.to_json_string([dictionary])
        result = (
                '[{{"x": 2, "width": 10, "id": {}, "height": 7, "y": 8}}]'
                .format(str(r1.id))
                )
        self.assertEqual(sorted(json_result), sorted(result))

    def test_to_json_string_edge_cases(self):
        # Test case: List with multiple dictionaries
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(5, 5, 1, 1)
        dictionary1 = r1.to_dictionary()
        dictionary2 = r2.to_dictionary()
        json_result_multiple = Base.to_json_string([dictionary1, dictionary2])
        result = (
                '[{{"x": 2, "width": 10, "id": {}, "height": 7, "y": 8}}, '
                '{{"x": 1, "width": 5, "id": {}, "height": 5, "y": 1}}]'
                .format(str(r1.id), str(r2.id))
                )
        self.assertEqual(sorted(json_result_multiple), sorted(result))

    def test_save_to_file_normal_case(self):
        """
        Test saving a list of Rectangle instances to a file.
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            content = file.read()
            expected = (
                    '[{{"y": 8, "x": 2, "id": {}, "width": 10, '
                    '"height": 7}}, {{"y": 0, "x": 0, "id": {}, "width": 2, '
                    '"height": 4}}]'.format(str(r1.id), str(r2.id))
            )
            self.assertEqual(json.loads(content), json.loads(expected))

    def test_save_to_file_empty_list(self):
        """
        Test saving an empty list to a file.
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[]')

    def test_save_to_file_with_None(self):
        """
        Test saving None to a file.
        """
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[]')

    def tearDown(self):
        # Clean up created files after each test
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

    def test_from_json_string_rectangle_normal_case(self):
        # Test case: Normal case for Rectangle
        json_string = '[{"id": 1, "width": 5, "height": 10, "x": 2, "y": 3}]'
        result = Rectangle.from_json_string(json_string)
        expected = [{'id': 1, 'width': 5, 'height': 10, 'x': 2, 'y': 3}]
        self.assertEqual(result, expected)

    def test_from_json_string_rectangle_empty_string(self):
        # Test case: Empty string for Rectangle
        json_string = ""
        result = Rectangle.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_rectangle_none(self):
        # Test case: None input for Rectangle
        json_string = None
        result = Rectangle.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_create_rectangle(self):
        """
        Test creating a Rectangle instance using the create class method.
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsInstance(r2, Rectangle)
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)

    def test_load_from_file_rectangle(self):
        """
        Test loading Rectangle instances from a file.
        """
        r1 = Rectangle(5, 10)
        r2 = Rectangle(3, 6)
        Rectangle.save_to_file([r1, r2])

        obj_list = Rectangle.load_from_file()
        self.assertEqual(len(obj_list), 2)
        self.assertIsInstance(obj_list[0], Rectangle)
        self.assertIsInstance(obj_list[1], Rectangle)

    def test_load_from_file_rectangle_with_parameters(self):
        """
        Test loading Rectangle instances with more parameters from a file.
        """
        r1 = Rectangle(5, 10, 2, 3, 99)
        r2 = Rectangle(3, 6, 0, 0, 42)
        Rectangle.save_to_file([r1, r2])

        obj_list = Rectangle.load_from_file()
        self.assertEqual(len(obj_list), 2)
        self.assertIsInstance(obj_list[0], Rectangle)
        self.assertIsInstance(obj_list[1], Rectangle)
        self.assertEqual(obj_list[0].id, 99)
        self.assertEqual(obj_list[1].id, 42)

    def test_save_and_load_from_file_csv_rectangle(self):
        """
        Test saving and loading Rectangle instances to and from a CSV file.
        """
        r1 = Rectangle(5, 10, 2, 7)
        r2 = Rectangle(3, 6, 1, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()

        for rect in list_rectangles_output:
            self.assertIsInstance(rect, Rectangle)
            self.assertIn(rect, list_rectangles_input)

    def test_save_and_load_from_file_csv_rectangle_empty(self):
        """
        Test saving and loading an empty list of Rectangle instances to and from a CSV file.
        """
        list_rectangles_input = []
    
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()

        self.assertEqual(list_rectangles_input, list_rectangles_output)

    def test_load_from_file_csv_nonexistent_file(self):
        """
        Test loading from a CSV file that does not exist and ensure that an empty list is returned.
        """
        filename = "Rectangle.csv"

        # Check if the file exists
        if os.path.exists(filename):
            # Remove the file if it exists
            os.remove(filename)

        # Assuming the file "NonexistentFile.csv" does not exist
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles_output, [])


if __name__ == '__main__':
    unittest.main()
