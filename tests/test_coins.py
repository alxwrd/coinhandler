import pytest

from coinhandler.coins import Coin, OnePound, OnePence, FivePence


def test_coins_are_equal():
    assert Coin(1) == Coin(1)


def test_coins_upgrade():
    assert OnePound(1) == Coin(100)


def test_100_pence_makes_1_pound():
    pound = OnePence(100)

    assert isinstance(pound, OnePound)


def test_coins_are_comparable_to_floats():
    pound = Coin(100)
    twenty = Coin(20)

    assert pound == 1.00
    assert twenty == 0.20


def test_coins_are_comparable_to_ints():
    pound = Coin(100)
    twenty = Coin(20)

    assert pound == 100
    assert twenty == 20


def test_coin_gets_correct_subclass():
    assert Coin(100) == OnePound(1)


def test_remove_coin_after_defined():
    class Quarter(Coin):
        multiplier = 25

    assert Coin(25).__class__ == Quarter

    Coin.remove_subcoin(Quarter)

    assert Coin(25).__class__ == FivePence
