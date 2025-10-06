import pytest

from app.calculation.calculation import Calculation, History
from app.calculation.factory import CalculationFactory, parse_operands


def test_calculation_result():
    from app.operation.operations import add
    calc = Calculation("add", add, (1, 2, 3))
    assert calc.result() == 6.0


def test_history_add_and_iter():
    h = History()
    c = CalculationFactory.create("add", [1, 2])
    h.add(c)
    assert list(h)[0] is c


@pytest.mark.parametrize("parts,expected", [
    (["1", "2", "3"], [1.0, 2.0, 3.0]),
    (["-1.5"], [-1.5]),
])
def test_parse_operands(parts, expected):
    assert parse_operands(parts) == expected


def test_factory_unknown_operation():
    with pytest.raises(ValueError):
        CalculationFactory.create("pow", [2, 3])


@pytest.mark.parametrize("op,operands", [
    ("add", [1]),
    ("+", [1, 2, 3]),
    ("multiply", [2, 3]),
])
def test_factory_variadic_ok(op, operands):
    calc = CalculationFactory.create(op, operands)
    assert pytest.approx(calc.result()) == calc.operation(*operands)


@pytest.mark.parametrize("op,operands", [
    ("subtract", [1]),
    ("divide", [1, 2, 3]),
])
def test_factory_binary_arity_validation(op, operands):
    with pytest.raises(ValueError):
        CalculationFactory.create(op, operands)


def test_factory_variadic_requires_at_least_one_operand():
    with pytest.raises(ValueError):
        CalculationFactory.create("add", [])


def test_history_len_and_iterate():
    # Covers len()/iter() even though they are trivial
    h = History()
    assert len(h) == 0
    assert list(h) == []

    c = CalculationFactory.create("add", [1, 2])
    h.add(c)
    assert len(h) == 1
    items = list(h)
    assert items and items[0] is c

    h.clear()
    assert len(h) == 0
    assert list(h) == []
