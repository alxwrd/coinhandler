import pytest

from coinhandler import CoinHandler, Pound, Pence, Transaction

test_coin_amounts = (200, 100, 50, 20, 5)

def test_starting_float_correct_total():
    handler = CoinHandler(starting_float=test_coin_amounts)

    assert handler.total() == sum(test_coin_amounts)


def test_starting_float_correct_coins():
    handler = CoinHandler(starting_float=test_coin_amounts)

    assert handler.available_coins == [Pound(2), Pound(1), Pence(50), Pence(20), Pence(5)]


def test_inserting_coins_doesnt_update_total():
    handler = CoinHandler(starting_float=test_coin_amounts)

    handler.insert(200)

    assert handler.total() == sum(test_coin_amounts)


def test_transaction_is_tracked():
    handler = CoinHandler(starting_float=test_coin_amounts)

    handler.insert(200)

    assert handler.current_transaction == Transaction(200)


def test_coins_are_returned():
    handler = CoinHandler(starting_float=test_coin_amounts)

    handler.insert(200)
    handler.return_coins()

    assert handler.current_transaction == Transaction()
    assert handler.total() == sum(test_coin_amounts)


def test_purchase_deducts_from_transaction():
    handler = CoinHandler(starting_float=test_coin_amounts)

    handler.insert(50)
    handler.insert(100)

    handler.purchase()

    assert handler.current_transaction == Transaction(20, 5)


def test_after_purchase_correct_amount_is_returned():
    handler = CoinHandler(starting_float=test_coin_amounts)

    handler.insert(50)
    handler.insert(100)

    handler.purchase()

    assert handler.return_coins() == [Pence(20), Pence(5)]


def test_after_purchase_correct_total():
    handler = CoinHandler(starting_float=test_coin_amounts)

    handler.insert(50)
    handler.insert(100)

    handler.purchase()

    assert handler.total() == 400


def test_after_purchase_correct_coins_remain():
    handler = CoinHandler(starting_float=test_coin_amounts)

    handler.insert(50)
    handler.insert(100)

    handler.purchase()

    assert handler.available_coins == [Pound(2), Pound(1), Pound(1), Pence(50), Pence(50)]

