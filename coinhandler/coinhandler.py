from .collections import CoinCollection, Transaction


class CoinHandler:

    def __init__(self, starting_float=()):
        self.available_coins = CoinCollection(*starting_float)
        self.current_transaction = Transaction()

    def total(self):
        return self.available_coins.total() / 100

    def insert(self, value):
        self.current_transaction.append(value)

    def purchase(self, value):

        purchase_value = CoinCollection.from_value(value)

        change = CoinCollection.from_value(
            self.current_transaction.total() - purchase_value.total()
        )

        self.available_coins.extend(self.current_transaction.clear())

        for coin in change:
            self.available_coins.remove(coin)
            self.current_transaction.append(coin)

    def return_coins(self):
        return self.current_transaction.clear()
