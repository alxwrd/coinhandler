
from .coins import Coin, coerce_other


class CoinCollection:

    def __init__(self, *coins):
        self.__coins = []
        for coin in coins:
            self.append(coin)

    @classmethod
    @coerce_other
    def from_value(cls, value):
        coins = []
        for klass in Coin.sub_coins():
            amount, value = divmod(value, klass.multiplier)
            if amount:
                coins.extend(Coin(klass.multiplier) for _ in range(amount))
        return cls(*coins)

    @coerce_other
    def remove_by_value(self, value):
        coins = []
        for coin in self.__coins:
            amount, value = divmod(value, coin.multiplier)
            if amount:
                coins.append(Coin(coin.multiplier))
                value = ((amount - 1) * coin.multiplier) + value
        for coin in coins:
            self.remove(coin)
        return self.__class__(*coins)

    @coerce_other
    def append(self, item):
        self.__coins.append(Coin(item))

    def extend(self, iterable):
        for item in iterable:
            self.append(item)

    @coerce_other
    def remove(self, item):
        self.__coins.remove(Coin(item))

    def clear(self):
        coins = self.__coins[:]
        self.__coins.clear()
        return CoinCollection(*coins)

    def pop(self, index=-1):
        return self.__coins.pop(index)

    def total(self):
        return sum(coin.value for coin in self.__coins)

    def __getitem__(self, index):
        return self.__coins[index]

    def __eq__(self, other):
        return sorted(self.__coins) == sorted(other)

    def __repr__(self):
        coins = ", ".join(repr(coin) for coin in self.__coins)
        return f"{self.__class__.__name__}({coins})"


class Transaction(CoinCollection):
    pass
