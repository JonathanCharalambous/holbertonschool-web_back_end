#!/usr/bin/env python3
from typing import Iterable, Sequence, List, Tuple

"""Return a list of the lengths of each element in the input iterable."""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    lst: The input iterable.
    Return: A list of the lengths of each element in lst.
    """
    return [(i, len(i)) for i in lst]