#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map function.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, MagicMock


class TestAccessNestedMap(unittest.TestCase):
    """
    Test for access_nested_map function
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test that access_nested_map return right
        the expected value
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """
        Test that keyError is raised when key is not found
        and that the exception message is correct.
        """

        # Check if the function raised a exception key Error
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        # Check that the key in the exception is correct
        self.assertEqual(context.exception.args[0], expected)


class TestGetJson(unittest.TestCase):
    """
    Test for get_json function.
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test that get_json returns expected JSON
        and that requests.get is called correctly.
        """
        mock_get.return_value.json.return_value = test_payload

        result = get_json(test_url)

        self.assertEqual(result, test_payload)

        mock_get.assert_called_once_with(test_url)
