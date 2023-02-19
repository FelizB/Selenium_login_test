import pytest


def add_two_numbers(a , b):
    return a+b


@pytest.mark.math
def test_small_numbers():
    assert add_two_numbers(1,2) == 3, "the sum of 1 + 2 should be 3 "


def test_large_numbers():
    assert add_two_numbers(100,300) == 400, " the sum of 100 and 400 should be 400"


