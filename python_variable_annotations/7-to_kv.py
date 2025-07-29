#!/usr/bin/env python3

def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """Return a tuple containing a string and the square of a number."""
    return (k, float(v ** 2))
