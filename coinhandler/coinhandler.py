from .coins import CoinCollection


class CoinHandler:

    def __init__(self, starting_float=()):
        self.available_coins = CoinCollection(*starting_float)
