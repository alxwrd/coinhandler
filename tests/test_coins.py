import pytest

from coinhandler import Coin, CoinCollection
from coinhandler.coins import OnePound, OnePence


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


def test_coin_collections_are_equal():
    assert CoinCollection(1, 2) == CoinCollection(1, 2)
