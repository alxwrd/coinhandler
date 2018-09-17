# Coinhandler :moneybag:

> A Python module to handle interacting with coins

[![Build Status](https://travis-ci.com/alxwrd/coinhandler.svg?branch=master)](https://travis-ci.com/alxwrd/coinhandler)

```python
>>> from coinhandler import CoinHandler

>>> handler = CoinHandler(
...     starting_float=(2.00, 1.00, 0.50, 0.20, 0.05)
... )

>>> handler.insert(0.50)
>>> handler.insert(1.00)

>>> handler.purchase(1.25)

>>> handler.return_coins()
CoinCollection(TwentyPence(1), FivePence(1))
```

## Installation

### [pipenv](https://github.com/pypa/pipenv)*

```shell
pipenv install coinhandler
```

### [pip](https://pypi.org/project/coinhandler)

```shell
pip install coinhandler
```

### From source
```shell
pip install git+git://github.com/alxwrd/coinhandler.git
```

> _*recommended_


## Useage

### CoinHandler

A `CoinHandler` object can be used to manage a transaction, or a series
of transactions. To create a handler instance, it should be provided
with a starting [float](https://en.wikipedia.org/wiki/Float_(money_supply))
(money supply).

The `starting_float` should be an _iterable_ of either `float` or `int`

```python
from coinhandler import CoinHandler

handler = CoinHandler(
    starting_float=(2.00, 1.00, 0.50, 0.20, 0.05)
)
```

A `CoinHandler` object provides a simple interface for making trasactions
against the float it started with.

#### `.available_coins` -> [`CoinCollection`](#coincollection)

Provides access to the current supply of `Coin`s in in the handler.

```python
>>> handler.available_coins
CoinCollection(TwoPound(1), OnePound(1), FiftyPence(1), TwentyPence(1), FivePence(1))
```

#### `.current_transaction` -> [`Transaction`](#transaction)

Provides access to the `Coin`s that are part of the current transaction.

```python
>>> handler.insert(0.50)
>>> handler.current_transaction
Transaction(FiftyPence(1))
```

#### `.total()` -> `float`

Returns the handlers current total value as a float.

```python
>>> handler.total()
3.75
```

Also equivalent to:

```python
>>> handler.available_coins.total() / 100
3.75
```

#### `.insert(` _`value`_ `)`

Add a coin of _value_ to the `current_transaction`.

```python
>>> handler.insert(0.50)
>>> handler.current_transaction
Transaction(FiftyPence(1))
```

#### `.purchase(` _`value`_ `)`

Moves the coins from `current_transaction` into the `available_coins` and
makes the difference in coins between the purchase _value_ and the
`current_transation.total()` available in `.current_transaction`.

```python
>>> handler.available_coins
CoinCollection(TwentyPence(1), FivePence(1))

>>> handler.insert(0.50)
>>> handler.purchase(0.25)

>>> handler.current_transaction
Transaction(TwentyPence(1), FivePence(1))
>>> handler.available_coins
CoinCollection(FiftyPence(1))
```

#### `.return_coins()` -> [`CoinCollection`](#coincollection)

Empties out the `current_transaction` and returns those coins as a
`CoinCollection`.



### CoinCollection

A `CoinCollection` object represents a collection of `Coin`s. It functions
similar to a python `list`, and provides some similar methods.


```python
from coinhandler import CoinCollection

collection = CoinCollection(2.00, 1.00, 0.50)
```

You can also create a `CoinCollection` from a value. This will return the
smallest amount of `Coin`s needed to create that value.

```python
>>> CoinCollection.from_value(1.25)
CoinCollection(OnePound(1), TwentyPence(1), FivePence(1))
```

#### `Transaction`

A `Transaction` object is a subclass of `CoinCollection`, and functions
identically.


#### `.remove_by_value(` _`value`_ `)` -> [`CoinCollection`](#coincollection)

Removes coins from the collection by a value, and returns new collection
with valid coins from the original collection.

```python
>>> collection = CoinCollection(2.00, 1.00, 0.20, 0.05)
>>> collection.remove_by_value(1.25)
CoinCollection(OnePound(1), TwentyPence(1), FivePence(1))
```

> NOTE: `.remove_by_value` will only remove available coins from
> the original collection. So for the example:
> ```python
> >>> collection = CoinCollection(2.00, 1.00, 0.20, 0.05)
> >>> collection.remove_by_value(1.30)
> CoinCollection(OnePound(1), TwentyPence(1), FivePence(0.05))
> ```
> Only '`1.25`' is returned.

#### `.total()`

Returns the total value of the collection as a _float_.

```python
>>> collection = CoinCollection(2.00, 1.00, 0.50)
>>> coins.total()
3.75
```


#### `.append(` _`value`_ `)`

Adds the _value_ to the collection.

```python
>>> collection = CoinCollection(2.00, 1.00, 0.50)
>>> collection.append(1.00)
>>> collection.total()
4.50
```


#### `.extend(` _`iterable[values]`_ `)`

Extends the collection by an _iterable_ of _values_.

```python
>>> collection = CoinCollection(2.00, 1.00, 0.50)
>>> collection.extend([1.00, 1.00])
>>> collection.total()
5.50
```


#### `.remove(` _`value`_ `)`

Removes a `Coin` represented by _value_ from the collection.

```python
>>> collection = CoinCollection(2.00, 1.00, 0.50)
>>> collection.remove(1.00)
>>> collection.total()
2.50
```


#### `.clear()` -> [`CoinCollection`](#coincollection)

Removes all `Coin`s from the collection, and returns them as a new collection.

```python
>>> collection = CoinCollection(2.00, 1.00, 0.50)
>>> coins = collection.clear()
>>> collection.total()
0.0
>>> coins.total()
3.50
```


#### `.pop(` _`index=-1`_ `)` -> [`Coin`](#coin)

Removes the `Coin` located _index_ out of the collection and returns it.

```python
>>> collection = CoinCollection(2.00, 1.00, 0.50)
>>> collection.pop()
FiftyPence(1)
>>> collection.pop(0)
TwoPound(1)
>>> coins.total()
1.00
```


#### As a _list_

For basic useage, a `CoinCollection` can be [_duck typed_](https://en.wikipedia.org/wiki/Duck_typing)
as a list. It can be:

Compared to an _iterable_ of _values_,

```python
>>> collection = CoinCollection(2.00, 1.00, 0.50)
>>> assert collection = [2.00, 1.00, 0.50]
>>> assert collection = (2.00, 1.00, 0.50)
```

Iterated over,

```python
>>> collection = CoinCollection(2.00, 1.00, 0.50)
>>> for coin in collection:
...     print(coin)
'£2.00'
'£1.00'
'50p'
```

And accessed by index.

```python
>>> collection = CoinCollection(2.00, 1.00, 0.50)
>>> collection[1]
OnePound(1)
```



### Coin

A `Coin` object represents a _value_. Its use allows representing money
using _int_ vs. _float_.

The `Coin` class is a factory class for all other _Coins_ that have been defined.
It will return the highest value coin of a given _value_.

```python
from coinhandler import Coin
from coinhandler.coins import OnePound, FiftyPence

assert Coin(100) == OnePound(1)
assert Coin(50) == FiftyPence(1)
```

When using the `Coin` factory class, a valid coin _value_ should be used. Not doing so
can create undesirable `Coin` objects.

```python
>>> coin = Coin(23)
OnePence(23)

# Use a CoinCollection instead!

>>> CoinCollection.from_value(23)
CoinCollection(TwentyPence(1), TwoPence(1), OnePence(1))
```

_Coins_ of a specfic type can be created by just by creating an instance of them.

```python
>>> from coinhandler.coins import OnePound
>>> OnePound()
OnePound(1)
```

All coins have a value, which is the represented as an _integer_.

```python
>>> from coinhandler.coins import OnePound
>>> OnePound().value
100
```

Subclassing from `Coin` will add that coin to the available coins to be created.

```python
>>> from coinhandler import Coin
>>> Coin(25)
FivePence(5)

>>> class Quarter(Coin):
...     multiplier = 25
...     def __str__(self):
...         return f"{self.value}¢"
>>> coin = Coin(25)
>>> print(coin)
'25¢'
>>> coin.value
25
