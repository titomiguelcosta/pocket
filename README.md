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

```
$ python bin/pocket profit 1000 --source=NZD --target=GBP

```