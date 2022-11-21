#!/usr/bin/python3
'''
function def island_perimeter(grid):
that returns the perimeter of the island described in grid:
grid is a list of list of integers:'''


def island_perimeter(grid):
    land = 0
    connect = 0
    for down in range(len(grid)):
        for across in range(len(grid[down])):
            if grid[down][across] == 1:
                land += 1
                if down > 0 and grid[down - 1][across] == 1:
                    connect += 1
                if across > 0 and grid[down][across - 1] == 1:
                    connect += 1
    return land * 4 - connect * 2
