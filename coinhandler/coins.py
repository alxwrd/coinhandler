
class Coin:
    multiplier = 1

    def __new__(cls, value):
        value *= cls.multiplier  # Adjust the value

        subclasses = sorted(
            Coin.__subclasses__(),
            key=lambda c: c.multiplier,
            reverse=True)

        for klass in subclasses:
            # If the classes multiplier is a multiple of the value,
            #  upgrade the new object to that type.
            if value % klass.multiplier == 0:
                coin = object.__new__(klass)
                coin.value = value
                return coin

    def __eq__(self, other):
        if isinstance(other, Coin):
            return self.value == other.value

        if isinstance(other, float):
            other = int(other * 100)
        return self.value == other

    def __repr__(self):
        return f"{self.__class__.__name__}({self.value // self.multiplier})"


class Pound(Coin):
    multiplier = 100

    def __str__(self):
        return f"£{self.value // self.multiplier}"


class Pence(Coin):
    multiplier = 1

    def __str__(self):
        return f"{self.value}p"


class CoinCollection:

    def __init__(self, *coins):
        self.__coins = []
        for coin in coins:
            self.append(coin)

    def append(self, item):
        if isinstance(item, int):
            item = Coin(item)
        if isinstance(item, float):
            item = Coin(int(item * 100))

        if not isinstance(item, Coin):
            raise ValueError(
                "Only 'int', 'float', or 'Coin' can be "
                "added to a 'CoinCollection'")
        self.__coins.append(item)

    def __eq__(self, other):
        return self.__coins == other

    def __repr__(self):
        coins = ", ".join(repr(coin) for coin in self.__coins)
        return f"{self.__class__.__name__}({coins})"


class Transaction(CoinCollection):
    pass
