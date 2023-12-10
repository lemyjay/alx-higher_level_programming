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

    def test_constructor_with_positive_id(self):
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

    def test_to_json_string(self):
        # Test case 1: Empty list of dictionaries
        json_result_empty = Base.to_json_string([])
        self.assertEqual(json_result_empty, '[]')

        # Test case 2: None as input
        json_result_none = Base.to_json_string(None)
        self.assertEqual(json_result_none, '[]')

    def test_to_json_string_edge_cases(self):
        # Test case: Ensure valid JSON syntax with various data types
        data = [
                {"name": "John", "age": 30, "city": "New York"},
                42, True, None, {"key": ["value1", "value2"]}
                ]
        json_result_varied_types = Base.to_json_string(data)
        result = '[{"name": "John", "age": 30, "city": "New York"}, 42,'
        result += ' true, null, {"key": ["value1", "value2"]}]'
        self.assertEqual(json_result_varied_types, result)


if __name__ == '__main__':
    unittest.main()
