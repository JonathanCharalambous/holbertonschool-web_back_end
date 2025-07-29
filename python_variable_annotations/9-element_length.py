#!/usr/bin/env python3
from typing import Iterable, Sequence, List

def element_length(lst: Iterable[Sequence]) -> List[int]:
    """Return a list of the lengths of each element in the input iterable."""
    return [len(i) for i in lst]
