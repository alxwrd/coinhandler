import pytest

import coinhandler
from coinhandler import CoinHandler

test_coin_amounts = (2.00, 1.00, 0.50, 0.20, 0.05)


def test_starting_float_correct_total():
    handler = CoinHandler(starting_float=test_coin_amounts)

    assert handler.total() == sum(test_coin_amounts)


def test_starting_float_correct_coins():
    handler = CoinHandler(starting_float=test_coin_amounts)

    assert handler.available_coins == test_coin_amounts


def test_inserting_coins_doesnt_update_total():
    handler = CoinHandler(starting_float=test_coin_amounts)

    handler.insert(2.00)

    assert handler.total() == sum(test_coin_amounts)


def test_transaction_is_tracked():
    handler = CoinHandler(starting_float=test_coin_amounts)

    handler.insert(2.00)

    assert handler.current_transaction == [2.00]


def test_coins_are_returned():
    handler = CoinHandler(starting_float=test_coin_amounts)

    handler.insert(2.00)
    handler.return_coins()

    assert handler.current_transaction == []
    assert handler.total() == sum(test_coin_amounts)


def test_correct_coins_are_returned():
    handler = CoinHandler(starting_float=test_coin_amounts)

    handler.insert(0.50)
    handler.insert(1.00)
    assert handler.return_coins() == [0.50, 1.00]


def test_purchase_deducts_from_transaction():
    handler = CoinHandler(starting_float=test_coin_amounts)

    handler.insert(0.50)
    handler.insert(1.00)

    handler.purchase(1.25)

    assert handler.current_transaction == [0.20, 0.05]


def test_after_purchase_correct_amount_is_returned():
    handler = CoinHandler(starting_float=test_coin_amounts)

    handler.insert(0.50)
    handler.insert(1.00)

    handler.purchase(1.25)

    assert handler.return_coins() == [0.20, 0.05]


def test_after_purchase_correct_total():
    handler = CoinHandler(starting_float=test_coin_amounts)

    handler.insert(0.50)
    handler.insert(1.00)

    handler.purchase(1.25)

    assert handler.total() == 5.00


def test_after_purchase_correct_coins_remain():
    handler = CoinHandler(starting_float=test_coin_amounts)

    handler.insert(0.50)
    handler.insert(1.00)

    handler.purchase(1.25)

    assert handler.available_coins == [2.00, 1.00, 1.00, 0.50, 0.50]


def test_correct_coins_when_float_doesnt_have_higher_values():
    handler = CoinHandler(starting_float=(0.50, 0.50, 0.50, 0.50))

    handler.insert(2.00)

    handler.purchase(1.00)

    assert handler.return_coins() == [0.50, 0.50]


def test_purchase_not_available_when_no_transaction():
    handler = CoinHandler(starting_float=test_coin_amounts)

    with pytest.raises(coinhandler.NotEnoughTransaction):
        handler.purchase(1.00)


def test_purchase_fails_and_returns_coins_when_insufficient_change():
    handler = CoinHandler(starting_float=(0.50, 0.50, 0.50, 0.50))

    handler.insert(0.50)

    with pytest.raises(coinhandler.NotEnoughChange):
        handler.purchase(0.20)

    assert handler.return_coins() == [0.50]
    assert handler.available_coins == [0.50, 0.50, 0.50, 0.50]
