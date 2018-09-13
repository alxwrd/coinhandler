from .coins import CoinCollection, Transaction


class CoinHandler:

    def __init__(self, starting_float=()):
        self.available_coins = CoinCollection(*starting_float)
        self.current_transaction = Transaction()

    def total(self):
        return self.available_coins.total() / 100

    def insert(self, value):
        self.current_transaction.append(value)

    def return_coins(self):
        coins = []
        while self.current_transaction.total():
            coins.append(self.current_transaction.pop(0))

        return CoinCollection(*coins)
