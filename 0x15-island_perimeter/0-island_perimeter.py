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
    """ returns the perimeter of the island described """
    perimeter = 0

    for water in range(len(grid)):
        for land in range(len(grid[water])):
            if grid[water][land] == 1:
                perimeter += 4
                if water > 0 and grid[water - 1][land] == 1:
                    water -= 2
                if land > 0 and grid[water][land - 1] == 1:
                    land -= 2
    return perimeter
