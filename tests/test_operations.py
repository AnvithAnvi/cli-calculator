import pytest
from app.operation.operations import add, subtract, multiply, divide

@pytest.mark.parametrize("args,expected", [
    ((1, 2, 3), 6.0),
    ((-1, 2.5), 1.5),
    (("1", "2", "3"), 6.0),
])
def test_add(args, expected):
    assert add(*args) == expected

@pytest.mark.parametrize("a,b,expected", [
    (5, 2, 3.0),
    ("10", "3", 7.0),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

@pytest.mark.parametrize("args,expected", [
    ((2, 3, 4), 24.0),
    (("1.5", "2"), 3.0),
    ((-1, 0), -0.0),
])
def test_multiply(args, expected):
    assert multiply(*args) == expected

def test_divide_ok():
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

@pytest.mark.parametrize("bad", [["a"], [None]])
def test_bad_numbers_raise(bad):
    from app.operation.operations import _coerce_numbers
    with pytest.raises(ValueError):
        _coerce_numbers(bad)
