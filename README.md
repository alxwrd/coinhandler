# coinhandler :moneybag:


## Example

```python
>>> from coinhandler import CoinHandler

>>> handler = CoinHandler(
...     starting_float=(2.00, 1.00, 0.50, 0.20, 0.05)
... )

>>> handler.total()
3.75

>>> handler.available_coins
[Pound(2), Pound(1), Pence(50), Pence(20), Pence(5)]

>>> handler.insert(0.50)
>>> handler.total()
3.75
>>> handler.current_transaction
<Transaction coins=Pence(50)>

>>> handler.return_coins()
[Pence(50)]

>>> handler.current_transaction
<Transaction coins=[]>

>>> handler.insert(0.50)
>>> handler.insert(1.00)
>>> handler.current_transaction
<Transaction coins=[Pence(50), Pound(1)]>

>>> handler.purchase(1.25)
>>> handler.current_transaction
<Transaction coins=[Pence(20), Pence(5)]>

>>> handler.return_coins()
[Pence(20), Pence(5)]

>>> handler.total()
4.00

>>> handler.available_coins
[Pound(2), Pound(1), Pound(1), Pence(50), Pence(50)]
```
