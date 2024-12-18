"""Imports utilities tests."""

from __future__ import annotations

import unittest

import package_name.utils.imports as imports_utils


class TestImportsUtils(unittest.TestCase):
    """Test cases for imports utilities."""

    def test_is_fire_available(self: TestImportsUtils) -> None:
        """Test case for `_is_fire_available`."""
        is_fire_available = imports_utils.is_fire_available
        assert is_fire_available
