# coinhandler :moneybag:


## Example

```python
>>> from coinhandler import CoinHandler

>>> handler = CoinHandler(
...     starting_float=(200, 100, 50, 20, 5)
... )

>>> handler.total()
375

>>> handler.available_coins
[Pound(2), Pound(1), Pence(50), Pence(20), Pence(5)]

>>> handler.insert(50)
>>> handler.total()
375
>>> handler.current_transaction
<Transaction coins=Pence(50)>

>>> handler.return_coins()
[Pence(50)]

>>> handler.current_transaction
<Transaction coins=[]>

>>> handler.insert(50)
>>> handler.insert(100)
>>> handler.current_transaction
<Transaction coins=[Pence(50), Pound(1)]>

>>> handler.purchase(125)
>>> handler.current_transaction
<Transaction coins=[Pence(20), Pence(5)]>

>>> handler.return_coins()
[Pence(20), Pence(5)]

>>> handler.total()
400

>>> handler.available_coins
[Pound(2), Pound(1), Pound(1), Pence(50), Pence(50)]
```
