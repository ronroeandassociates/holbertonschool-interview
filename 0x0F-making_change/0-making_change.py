#!/usr/bin/python3
'''
Prototype: def makeChange(coins, total)
Return: fewest number of coins needed to meet total
'''


def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        while total >= coin:
            total -= coin
            num_coins += 1
# If the total is not 0, then it means that the total cannot be met
# by any number of coins you have,
# so return -1.
    return -1 if total != 0 else num_coins
