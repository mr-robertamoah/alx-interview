#!/usr/bin/python3
"""
A module that contains pascal_triangle function
"""

def pascal_triangle(n):
    """
    return a list of lists 
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(1, n + 1): # loop 1 to n
        if i == 1:
            triangle.append([1])
        else:
            row = []
            for j in range(1, i + 1): # loop 1 to the current row
                if j == 1 or j == i:
                    row.append(1)
                else:
                    prev_list = triangle[i - 2]
                    idx = j - 2
                    row.append(prev_list[idx] + prev_list[idx + 1])
            triangle.append(row)

    return triangle
