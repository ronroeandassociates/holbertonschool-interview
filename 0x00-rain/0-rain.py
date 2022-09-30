#!/usr/bin/python3

"""
Given a list of non-negative integers representing the heights of walls
with unit width 1 calculate how many square units of water will be retained
after it rains.
Prototype: def rain(walls)
walls is a list of non-negative integers.
Return: Integer indicating total amount of rainwater retained.
If the list is empty return 0.
"""


def rain(walls):
    """Calculate units of water will be retained"""
    if not walls:
        return 0
    water = 0
    for i in range(1, len(walls) - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]
        for j in range(i + 1, len(walls)):
            right = max(right, walls[j])
        water += min(left, right) - walls[i]
    return water
