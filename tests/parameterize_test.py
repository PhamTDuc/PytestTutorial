import pytest


@pytest.mark.parametrize("val1, val2, result", ((5, 5, 10), (3, 5, 9)))
def test_addition(val1, val2, result):
    assert val1 + val2 == result, "Failed"
