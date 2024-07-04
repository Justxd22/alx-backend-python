#!/usr/bin/env python3
"""Multiply floats."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiply floats."""
    return lambda x: x * multiplier
