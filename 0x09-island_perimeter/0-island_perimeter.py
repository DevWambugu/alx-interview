#!/usr/bin/python3
'''0-island_perimeter'''


def island_perimeter(grid):
    '''This function returns
    the perimeter of the island described in grid.
    Args:
    grid: a list of list of integers'''
    if not grid:
        return 0
    '''Initialize the perimeter variable to zero'''
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])
    for row in range(rows):
        for column in range(cols):
            '''Each land cell contributes 4
            to the perimeter'''
            if grid[row][column] == 1:
                perimeter += 4
                '''Subract 2 if there are
                shared sides'''
                if row > 0 and grid[row - 1][column] == 1:
                    perimeter -= 2
                if column > 0 and grid[row][column - 1] == 1:
                    perimeter -= 2
    return perimeter
