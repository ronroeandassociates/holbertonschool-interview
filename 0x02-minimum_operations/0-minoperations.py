#!/usr/bin/python3

"""
0 Minimum Operations

In a text file, there is a single character H. Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to
result in exactly n H characters in the file

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""

def minOperations(n):
    """minOperations is a function that takes a number and returns the minimum number of operations needed to achieve it"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return minOperations(n-1) + minOperations(n-2) + 1
