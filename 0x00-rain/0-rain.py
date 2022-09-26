#!/usr/bin/python3
"""
0_rain
"""

def rain(walls):
    if len(walls) < 1:
        return 0

    # Find the highest wall
    amount = 0


for key, value in enumerate(walls):
    if key in [0, len(walls) - 1]:
        continue
    left = max(walls[:key])
    right = max(walls[key + 1:])
    if value < left and value < right:
        amount += min(left, right) - value
