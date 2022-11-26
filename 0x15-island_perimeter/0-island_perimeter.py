#!/usr/bin/python3

'''
function def island_perimeter(grid):
that returns the perimeter of the island described in grid:
grid is a list of list of integers:
        0 represents water
        1 represents land
        Each cell is square, with a side length of 1
        Cells are connected horizontally/vertically (not diagonally).
        grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesnt have “lakes”
        (water inside that isnt connected to the
            water surrounding the island).
'''


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid"""
    perimeter = 0
    for i in range(len(grid)):
        for land in range(len(grid[i])):
            if grid[i][land] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][land] == 1:
                    perimeter -= 2
                if land > 0 and grid[i][land - 1] == 1:
                    perimeter -= 2
    return perimeter
