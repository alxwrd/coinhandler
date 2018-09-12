import pytest

from coinhandler import Pound, Pence, Coin


def test_pounds_are_equal():
    assert Pound(1) == Pound(1)


def test_pounds_equal_pence():
    assert Pound(1) == Pence(100)


def test_100_pence_makes_1_pound():
    pound = Pence(100)

    assert isinstance(pound, Pound)


def test_coins_are_comparable_to_floats():
    pound = Pound(1)
    pence = Pence(20)

    assert pound == 1.00
    assert pence == 0.20


def test_coins_are_comparable_to_ints():
    pound = Pound(1)
    pence = Pence(20)

    assert pound == 100
    assert pence == 20


def test_coin_gets_correct_subclass():
    assert Coin(100) == Pound(1)


def test_new_subtypes_of_coin():
    class Fifty(Coin):
        multiplier = 50

    assert Coin(50) == Fifty(1)


def test_coin_can_get_correct_subclass_from_new_coins():
    class Fifty(Coin):
        multiplier = 50

    class Twenty(Coin):
        multiplier = 20

    class Ten(Coin):
        multiplier = 10

    assert Coin(50) == Fifty(1)
    assert Coin(20) == Twenty(1)
    assert Coin(10) == Ten(1)
