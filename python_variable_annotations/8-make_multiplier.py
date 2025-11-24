#!/usr/bin/env python3
"""
Module contains a function that takes a float
as argument and returns a function that multiplies a float.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by multiplier.
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
