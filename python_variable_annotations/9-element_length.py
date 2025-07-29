#!/usr/bin/env python3
from typing import Iterable, Sequence, List

def element_length(lst: Iterable[Sequence]) -> List[int]:
    return [len(i) for i in lst]