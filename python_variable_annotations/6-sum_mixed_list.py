#!/usr/bin/env python3
"""
module that contains a function which takes a list
of integers and floats and returns their sum as a float.
"""
from typing import Union


def sum_mixed_list(mxd_ls: list[int | float]) -> float:
    return sum(mxd_ls)
