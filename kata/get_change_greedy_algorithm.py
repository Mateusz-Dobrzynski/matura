def getChange(coinsSet: list, value: float):
    moneyToBeChanged = value
    change = []
    for coin in coinsSet:
        while coin <= moneyToBeChanged:
            change.append(coin)
            moneyToBeChanged -= coin
    return change


"""
The coin set is based upon denominations available in Polish currency.
No vending machine would use all of them, of course, as their value/mass ratio drastically decreases at lower denominations
"""
assert getChange([500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.1, 0.05, 0.02, 0.01], 50) == [50]
assert getChange([500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.1, 0.05, 0.02, 0.01], 1234) == [500, 500, 200, 20, 10, 2, 2]
assert getChange([500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.1, 0.05, 0.02, 0.01], 1984) == [500, 500, 500, 200, 200, 50, 20, 10, 2, 2]
assert getChange([500, 200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.20, 0.1, 0.05, 0.02, 0.01], 21.37) == [20, 1, 0.20, 0.1, 0.05, 0.02]
