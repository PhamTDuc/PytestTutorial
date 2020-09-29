import pytest


@pytest.mark.group2
def test_method0():
    x, y = 5, 6
    assert x + 1 == y, "Test Addition, assertion failed"
    assert x == y, "Assertion failed"


@pytest.mark.group1
def test_method1():
    x, y = 5, 6
    assert x + 1 == y, "Test test_method1 failed"


@pytest.mark.group2
def test_methods2():
    x, y = 5, 6
    assert x + 1 == y, "Test Addition, assertion failed"
    assert x == y, "Assertion failed"


@pytest.mark.xfail
def test_methods3():
    x, y = 5, 7
    assert x + 1 == y, "Test test_method1 failed"
