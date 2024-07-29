#!/usr/bin/env python3
"""Unitests for utils."""


from typing import Dict
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import (
    access_nested_map,
    get_json,
    memoize,
)


class TestAccessNestedMap(unittest.TestCase):
    """Test Access Nested func."""

    @parameterized.expand([
       ({"a": 1}, ("a",), 1),
       ({"a": {"b": 2}}, ("a",), {"b": 2}),
       ({"a": {"b": 2}}, ("a", "b",), 2),
    ])
    def test_access_nested_map(self, nmap: Dict, path: Dict, ans: any) -> None:
        """Test Access Nested func."""
        self.assertEqual(access_nested_map(nested_map=nmap, path=path), ans)

    @parameterized.expand([
       ({}, ("a",)),
       ({"a": 1}, ("a", "b",)),
    ])
    def test_access_nested_map_exception(self, nmap: Dict, path: Dict) -> None:
        """Test Access Nested func."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map=nmap, path=path)


class TestGetJson(unittest.TestCase):
    """Test get_json func."""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url: str, payload: Dict) -> None:
        """Test get_json func."""
        attrs = {'json.return_value': payload}
        with patch("requests.get", return_value=Mock(**attrs)) as req_get:
            self.assertEqual(get_json(test_url), payload)
            req_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Test memoize func."""
    def test_memoize(self) -> None:
        """Test memoize func."""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, "a_method", return_value=lambda: 42,) \
                as memo_fxn:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memo_fxn.assert_called_once()
