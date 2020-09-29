import pytest


def test_compareA(supplier):
    z = 35
    assert supplier[0] == z, "a and z comparison failed"


def test_compareB(supplier):
    z = 35
    assert supplier[1] == z, "b and z comparison failed"


def test_compareC(supplier):
    z = 35
    assert supplier[2] == z, "c and z comparison failed"
