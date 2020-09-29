import pytest


def test_compare_newA(supplier):
    z = 35
    assert supplier[0] == z, "a and z comparison failed"


def test_compare_newB(supplier):
    z = 35
    assert supplier[1] == z, "b and z comparison failed"


def test_compare_newC(supplier):
    z = 35
    assert supplier[2] == z, "c and z comparison failed"
