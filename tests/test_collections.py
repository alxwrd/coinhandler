
from coinhandler.collections import CoinCollection, Transaction


def test_coin_collections_are_equal():
    assert CoinCollection(1, 2) == CoinCollection(1, 2)


def test_creating_collection_from_value():
    assert CoinCollection.from_value(1.25) == CoinCollection(100, 20, 5)


def test_appending_to_collection():
    collection = CoinCollection(1, 2)

    collection.append(3)

    assert collection == CoinCollection(1, 2, 3)


def test_extending_collection():
    collection = CoinCollection(1, 2)

    collection.extend([3, 4])

    assert collection == CoinCollection(1, 2, 3, 4)


def test_removing_coins_from_collection():
    collection = CoinCollection(1, 2)

    collection.remove(1)

    assert collection == CoinCollection(2)


def test_collection_equal_to_list():
    assert CoinCollection(1, 2, 3) == [1, 2, 3]


def test_remove_by_value():
    collection = CoinCollection(20, 20, 10)

    removed = collection.remove_by_value(0.50)

    assert removed == [0.20, 0.20, 0.10]
