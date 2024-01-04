#!/usr/bin/python3
"""
Pascal's triangle
"""


def pascal_triangle(n):
    '''Returns the pascal's triangle of n'''
    triangle = []
    if n <= 0:
        return []
    else:
        for integer in range(n):
            '''initialize the row with ones'''
            row = [1] * (integer + 1)
            for number in range(1, integer):
                '''define row'''
                part1 = triangle[integer-1][number-1]
                part2 = triangle[integer-1][number]
                row[number] = part1 + part2
            triangle.append(row)
    return triangle
