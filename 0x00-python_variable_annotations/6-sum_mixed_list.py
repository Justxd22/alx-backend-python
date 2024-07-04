#!/usr/bin/env python3
"""Calc sum of list int/floats."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Calc sum of list int/floats."""
    return float(sum(mxd_lst))
