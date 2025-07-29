#!/usr/bin/env python3
from typing import Iterable, Sequence, List

"""Return a list of the lengths of each element in the input iterable."""


def element_length(lst: Iterable[Sequence]) -> List[int]:
    """
    lst: The input iterable.
    Return: A list of the lengths of each element in lst.
    """
    return [len(i) for i in lst]
