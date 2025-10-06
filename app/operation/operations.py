"""Low-level arithmetic operations (pure, easy to test)."""
from __future__ import annotations
from typing import Iterable, List

def _coerce_numbers(values: Iterable[float | int | str]) -> List[float]:
    """LBYL: ensure all values can convert to float."""
    nums: List[float] = []
    for v in values:
        try:
            nums.append(float(v))
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Invalid number: {v!r}") from exc
    return nums

def add(*args: float | int | str) -> float:
    nums = _coerce_numbers(args)
    return sum(nums)

def subtract(a: float | int | str, b: float | int | str) -> float:
    a_f, b_f = _coerce_numbers([a, b])
    return a_f - b_f

def multiply(*args: float | int | str) -> float:
    nums = _coerce_numbers(args)
    result = 1.0
    for n in nums:
        result *= n
    return result

def divide(a: float | int | str, b: float | int | str) -> float:
    a_f, b_f = _coerce_numbers([a, b])
    try:
        return a_f / b_f  # EAFP: let ZeroDivisionError happen
    except ZeroDivisionError as exc:
        raise ZeroDivisionError("Division by zero is not allowed") from exc
