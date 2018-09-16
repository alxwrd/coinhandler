
from coinhandler import CoinHandler, NotEnoughTransaction

if __name__ == "__main__":

    handler = CoinHandler(
        starting_float=(2.00, 1.00, 0.50, 0.20, 0.10, 0.05, 0.02, 0.01)
    )

    while True:
        coin = input("Insert a coin: ")

        if not coin:
            break

        try:
            handler.insert(float(coin))
        except ValueError:
            print(f"{coin} is not a valid value.")

    while True:
        purchase_amount = input("How much does it cost? ")

        try:
            purchase_amount = float(purchase_amount)
        except ValueError:
            print(f"'{purchase_amount}' is not a valid value.")

        if isinstance(purchase_amount, float):
            break

    try:
        handler.purchase(purchase_amount)
    except NotEnoughTransaction:
        print("You don't have enough to purchase that amount!")

    print("Your change is: ")

    print(", ".join(str(coin) for coin in handler.return_coins()))
