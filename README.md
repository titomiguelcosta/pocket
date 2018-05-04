Pocket
======

Python scripts to help make decisions when exchanging currencies.


Available commands
------------------

## Transfer

How much you get by transferring a certain amount.

```
$ python bin/pocket transfer 1000 --source=NZD --target=GBP
```

## Rate

What's the current rate between two currencies.

```
$ python bin/pocket rate --source=NZD --target=GBP
```

## Fees

How much will be the fees for transferring a certain amount.

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

## Balance

Determines the balance after reverting a transfer.
In the example, it is intended to determine how much it will be made by transferring back 9200NZD to the GBP account at the current rate.

```
$ python bin/pocket balance 5000 9200 --source=GBP --target=NZD

```
