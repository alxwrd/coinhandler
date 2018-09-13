from .coins import CoinCollection


class CoinHandler:

    def __init__(self, starting_float=()):
        self.available_coins = CoinCollection(*starting_float)

    def total(self):
        return self.available_coins.total() / 100
