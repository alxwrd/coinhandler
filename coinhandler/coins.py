
class Coin:

    def __new__(cls, value):
        coin = object.__new__(cls)

        if isinstance(coin, Pence) and value >= 100:
            coin = object.__new__(Pound)
            value /= 100

        coin.__init__(value)
        return coin

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, Coin):
            return self.value == other.value

        if isinstance(other, float):
            other = int(other * 100)
        return self.value == other


class Pound(Coin):

    def __init__(self, value):
        super().__init__(value * 100)


class Pence(Coin):
    pass


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



class Transaction(CoinCollection):
    pass
