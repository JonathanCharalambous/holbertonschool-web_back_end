#!/usr/bin/env python3
"""Return the sum of a mixed list of integers and floating-point numbers."""

from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """
    mxd_lst: A mixed list of integers and floating-point numbers.
    Return: The sum of all elements in mxd_lst.
    """
    return sum(mxd_lst)
