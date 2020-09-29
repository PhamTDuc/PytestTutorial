import pytest


@pytest.fixture
def supplier():
    a, b, c = 25, 35, 45
    return a, b, c
