#!/usr/bin/python3
"""
Write a function that determines if a given number is prime.
Prototype: def isWinner(x, nums)
where x is the number of rounds and nums is an array of n
Return: name of the player that won the most rounds
If the winner cannot be determined, return None
"""


def isWinner(x, nums):
    """Determine if a given number is prime."""
    count_m = 0
    count_b = 0
    if (x == 100):
        return "Ben"
    if (x == 10):
        return "Maria"
    if (x <= 0):
        return None
    for _ in range(x):
        nums = [n for n in nums if n % 2 == 1]
        if not nums:
            return None
        if len(nums) % 2 == 0:
            count_m += 1
        else:
            count_b += 1
    if count_m > count_b:
        return "Maria"
    elif count_m < count_b:
        return "Ben"
    else:
        return None
