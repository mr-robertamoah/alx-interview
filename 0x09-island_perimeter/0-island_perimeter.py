#!/usr/bin/python3
"""
Island perimeter computing module.
"""


def island_perimeter(grid):
    """Computes the perimeter of an island with no lakes."""
    if not isinstance(grid, list):
        return 0

    perimeter = 0
    rows = len(grid)

    for i, row in enumerate(grid):
        columns = len(row)

        for j, cell in enumerate(row):
            if cell == 0:
                continue

            # Check top
            if i == 0 or (grid[i - 1][j] == 0 if len(grid[i - 1]) > j else True):
                perimeter += 1

            # Check right
            if j == columns - 1 or (row[j + 1] == 0):
                perimeter += 1

            # Check bottom
            if i == rows - 1 or (grid[i + 1][j] == 0 if len(grid[i + 1]) > j else True):
                perimeter += 1

            # Check left
            if j == 0 or (row[j - 1] == 0):
                perimeter += 1

    return perimeter
