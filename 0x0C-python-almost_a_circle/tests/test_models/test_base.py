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

    def test_from_json_string_normal_case(self):
        # Test case: Normal case for Base
        json_string = '[{"id": 1}, {"id": 2}]'
        result = Base.from_json_string(json_string)
        expected = [{'id': 1}, {'id': 2}]
        self.assertEqual(result, expected)

    def test_from_json_string_empty_string(self):
        # Test case: Empty string for Base
        json_string = ""
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_from_json_string_none(self):
        # Test case: None input for Base
        json_string = None
        result = Base.from_json_string(json_string)
        self.assertEqual(result, [])

    def test_create_with_id(self):
        """
        Test creating a Base instance with an explicit ID using the create class method.
        """
        obj = Base(42)
        obj_dict = obj.to_dictionary()
        new_obj = Base.create(**obj_dict)
        self.assertIsInstance(new_obj, Base)
        self.assertIsNot(obj, new_obj)
        self.assertEqual(obj.id, new_obj.id)

    def test_create_with_empty_dict(self):
        """
        Test creating a Base instance with an empty dictionary using the create class method.
        """
        obj = Base.create()
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 1)

    def test_create_with_custom_attributes(self):
        """
        Test creating a Base instance with custom attributes using the create class method.
        """
        obj = Base.create(custom_attr="test")
        self.assertIsInstance(obj, Base)
        self.assertEqual(obj.id, 2)  # Default ID is 1, and the nb_objects is incremented
        self.assertEqual(obj.custom_attr, "test")


if __name__ == '__main__':
    unittest.main()
