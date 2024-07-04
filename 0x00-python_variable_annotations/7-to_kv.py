#!/usr/bin/env python3
"""Str to tuble func."""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Str to tuble func."""
    return (k, float(v**2))
