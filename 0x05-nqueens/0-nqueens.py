#!/usr/bin/python3
'''0-nqueens'''


import sys


def column_validity(board, row, col):
    '''This function checks if placing
    a queen in a certain column is valid'''
    for i in range(row):
        if board[i] == col:
            return False

        if abs(i - row) == abs(board[i] - col):
            return False
    return True


def solve_n_queens(n, board, row, solutions):
    '''This function solves the n-queens
    problem'''
    if row == n:
        solutions.append([[i, board[i]] for i in range(n)])
        return
    for col in range(n):
        if column_validity(board, row, col):
            board[row] = col
            solve_n_queens(n, board, row + 1, solutions)
            board[row] = -1


def main():
    '''This function calls the above functions
    to solve the puzzle'''
    if len(sys.argv) != 2:
        '''Check if the user gives 2 arguments'''
        print("Total arguments should be 2", file=sys.stderr)
        sys.exit(1)
    try:
        '''Check if the secon argumnet is a number'''
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number", file=sys.stderr)
        sys.exit(1)
    if n < 4:
        '''Check if 4 is the lowest number given'''
        print("N should be at least 4", file=sys.stderr)
        sys.exit(1)
    if not 1 <= n <= 32:
        '''N must be between 1 and 32. This part takes
        care of overflows.'''
        print("N must be between 1 and 32", file=sys.stderr)
        sys.exit(1)
    board = [-1] * n
    solutions = []
    solve_n_queens(n, board, 0, solutions)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
