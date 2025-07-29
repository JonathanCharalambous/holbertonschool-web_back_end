#!/usr/bin/env python3

def to_kv(k: str, v: int | float) -> tuple[str, float]:
    return (k, float(v ** 2))