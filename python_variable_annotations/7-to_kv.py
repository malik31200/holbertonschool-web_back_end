#!/usr/bin/env python3
"""
Module contains a function that takes a string and
an int OR float as arguments and returns a tuple.
"""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """
    Return a tuple with the first element of the tuple is the string.
    The second element is the square of the int/float v.
    and should be annotated as a float.
    """
    return (k, v ** 2)
