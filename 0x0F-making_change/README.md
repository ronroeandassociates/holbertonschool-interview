![0x0F-making_change_banner](https://github.com/ronroeandassociates/assets/blob/master/images/0x0F-making_change_banner.png)

# 0x0F. Making Change

## 0. Change comes from within

Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount `total`.

- Prototype: `def makeChange(coins, total)`
- Return: fewest number of coins needed to meet `total`
  - If `total` is `0` or less, return `0`
  - If `total` cannot be met by any number of coins you have, return `-1`
- `coins` is a list of the values of the coins in your possession
- The value of a coin will always be an integer greater than `0`
- assume have an infinite number of each denomination of coin in the list
- The solution’s runtime will be evaluated in this task
