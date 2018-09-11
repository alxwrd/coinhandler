import pytest

from coinhandler import Pound, Pence


def test_pounds_are_equal():
    assert Pound(1) == Pound(1)


def test_pounds_equal_pence():
    assert Pound(1) == Pence(100)


def test_100_pence_makes_1_pound():
    pound = Pence(100)

    assert isinstance(pound, Pound)


def coins_are_comparable_to_ints():
    pound = Pound(1)
    pence = Pence(20)

    assert pound == 1.00
    assert pence == 0.20

