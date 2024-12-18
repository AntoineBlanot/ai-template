"""Imports utilities."""

import importlib.util


def _is_package_available(pkg_name: str) -> bool:
    """Check if a package exists."""
    return importlib.util.find_spec(pkg_name) is not None


is_fire_available = _is_package_available("fire")
