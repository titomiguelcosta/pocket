Pocket
======

Python scripts to calculate exchange rates.


Available commands
------------------

## Transfer

```
$ python bin/pocket transfer 1000 --source=NZD --target=GBP
```

## Rate

```
$ python bin/pocket rate --source=NZD --target=GBP
```

## Fees

```
$ python bin/pocket fees 1000 --source=NZD --target=GBP

```

## Profit

Determines the rate needed to make a certain profit.
If --cashed parameter is not passed, it will use current rate to calculate initial transfer from source to target.
In the example, it is intended to make a profit of 100NZD by transfering 1000NZD to GBP and then transfering back.

```
$ python bin/pocket profit 100 1000 --source=NZD --target=GBP

```
