
def coerce_other(func):
    def wrapper(self, other):
        if isinstance(other, Coin):
            other = other.value

        if isinstance(other, float):
            other = int(other * 100)
        return func(self, other)
    return wrapper


class Coin:
    multiplier = 1

    def __new__(cls, value=1):
        value *= cls.multiplier  # Adjust the value

        for klass in Coin.sub_coins():
            # If the classes multiplier is a multiple of the value,
            #  upgrade the new object to that type.
            if value % klass.multiplier == 0:
                coin = object.__new__(klass)
                coin.value = value
                return coin

    @classmethod
    def sub_coins(cls):
        return sorted(
            Coin.__subclasses__(),
            key=lambda c: c.multiplier,
            reverse=True)

    @property
    def amount(self):
        return self.value // self.multiplier

    @coerce_other
    def __eq__(self, other):
        return self.value == other

    @coerce_other
    def __lt__(self, other):
        return self.value < other

    def __repr__(self):
        return f"{self.__class__.__name__}({self.amount})"


class TwoPound(Coin):
    multiplier = 200

    def __str__(self):
        return f"£{self.value // self.multiplier}"


class OnePound(Coin):
    multiplier = 100

    def __str__(self):
        return f"£{self.value // self.multiplier}"


class FiftyPence(Coin):
    multiplier = 50

    def __str__(self):
        return f"{self.value}p"


class TwentyPence(Coin):
    multiplier = 20

    def __str__(self):
        return f"{self.value}p"


class TenPence(Coin):
    multiplier = 10

    def __str__(self):
        return f"{self.value}p"


class FivePence(Coin):
    multiplier = 5

    def __str__(self):
        return f"{self.value}p"


class TwoPence(Coin):
    multiplier = 2

    def __str__(self):
        return f"{self.value}p"


class OnePence(Coin):
    multiplier = 1

    def __str__(self):
        return f"{self.value}p"
