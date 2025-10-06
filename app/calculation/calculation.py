"""Calculation objects and history management."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Sequence, List


@dataclass(frozen=True, slots=True)
class Calculation:
    """Represents a single arithmetic calculation."""
    operation_name: str
    operation: Callable[..., float]
    operands: Sequence[float]

    def result(self) -> float:
        return self.operation(*self.operands)


class History:
    """In-memory session history of calculations."""
    def __init__(self) -> None:
        self._items: List[Calculation] = []

    def add(self, calc: Calculation) -> None:
        self._items.append(calc)

    def clear(self) -> None:
        self._items.clear()

    def __iter__(self):  # pragma: no cover
        return iter(self._items)

    def __len__(self) -> int:  # pragma: no cover
        return len(self._items)
