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
        purchase_value = CoinCollection.from_value(value).total()

        if self.current_transaction.total() < purchase_value:
            raise NotEnoughTransaction(
                f"The amount {self.current_transaction.total()} "
                f"is not enough to cover {purchase_value}"
                )

        target_change = self.current_transaction.total() - purchase_value

        change = self.available_coins.remove_by_value(target_change)

        if change.total() != target_change:
            self.available_coins.extend(change)
            raise NotEnoughChange(
                "There is not enough available change to cover the transaction"
                )

        self.available_coins.extend(self.current_transaction.clear())

        for coin in change:
            self.current_transaction.append(coin)

    def return_coins(self):
        return self.current_transaction.clear()


class NotEnoughTransaction(Exception):
    pass


class NotEnoughChange(Exception):
    pass
