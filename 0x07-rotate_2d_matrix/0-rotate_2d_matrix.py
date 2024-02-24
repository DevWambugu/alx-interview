#!/usr/bin/python3
'''0-rotate_2d_matrix'''


def transpose_matrix(matrix, n):
    '''Create a function to transpose the
    matrix'''
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def reverse_matrix(matrix):
    '''Create a function to reveerse the matrix'''
    for row in matrix:
        row.reverse()


def rotate_2d_matrix(matrix):
    '''Call the 2 functions to rotate the matrix'''
    '''Get the length of the matrix'''
    n = len(matrix)
    '''Call the predefined functions
    to rotate the matrix'''
    transpose_matrix(matrix, n)
    reverse_matrix(matrix)
    return matrix

def print_matrix(matrix):
    '''Print the matrix with proper formatting'''
    for row in matrix:
        print("[", end="")
        for element in row:
            print(element, end=", ")
        print("\b\b],")
