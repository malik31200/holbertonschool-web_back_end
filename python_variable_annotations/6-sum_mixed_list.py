#!/usr/bin/env python3
"""
Module that contains a function which takes a list
of integers and floats and returns their sum as a float.
"""
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
