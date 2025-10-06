"""Factory to build Calculation from a user token + operands."""
from __future__ import annotations
from typing import Sequence, Tuple, Callable, Dict, List
from app.calculation.calculation import Calculation
from app.operation import operations

_OPS: Dict[str, Tuple[str, Callable[..., float]]] = {
    "add": ("add", operations.add), "+": ("add", operations.add), "sum": ("add", operations.add),
    "subtract": ("subtract", operations.subtract), "-": ("subtract", operations.subtract), "minus": ("subtract", operations.subtract),
    "multiply": ("multiply", operations.multiply), "*": ("multiply", operations.multiply), "times": ("multiply", operations.multiply),
    "divide": ("divide", operations.divide), "/": ("divide", operations.divide),
}

def normalize_token(token: str) -> str:
    return token.strip().lower()

def parse_operands(parts: Sequence[str]) -> List[float]:
    nums: List[float] = []
    for p in parts:
        try:
            nums.append(float(p))
        except ValueError as exc:
            raise ValueError(f"Non-numeric operand: {p!r}") from exc
    return nums

class CalculationFactory:
    @staticmethod
    def create(op_token: str, operands: Sequence[float]) -> Calculation:
        token = normalize_token(op_token)
        try:
            name, func = _OPS[token]
        except KeyError as exc:
            raise ValueError(f"Unknown operation: {op_token!r}") from exc
        # LBYL: arity checks
        if name in {"subtract", "divide"}:
            if len(operands) != 2:
                raise ValueError(f"{name} requires exactly 2 operands; got {len(operands)}")
        elif len(operands) < 1:
            raise ValueError(f"{name} requires at least 1 operand")
        return Calculation(operation_name=name, operation=func, operands=operands)
