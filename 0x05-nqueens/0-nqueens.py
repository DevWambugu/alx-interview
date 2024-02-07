#!/usr/bin/python3
'''0-nqueens'''


import sys


def column_validity(column, queens):
    '''This function checks if placing
    a queen in a certain column is valid'''
    for row, other_col in queens:
        '''Check if the queens are in the
        same row, column, or diagonal'''
        if column == other_col or \
                abs(column - other_col) == abs(row - other_col):
            return False
    return True


def solve_n_queens(n, column, queens):
    '''This function solves the n-queens
    problem'''
    global solutions
    if column == n:
        '''Print a solution if all queens are placed'''
        solutions.append([queen[0] for queen in queens])
        return
    for row in range(n):
        '''for each row, try placing a queen in each
        row of the current column'''
        if column_validity(column, queens):
            queens.append((row, column))
            solve_n_queens(n, column + 1, queens)
            queens.pop()


'''Store the solutions'''
solutions = []


def main():
    '''This function calls the above functions
    to solve the puzzle'''
    if len(sys.argv) != 2:
        '''Check if the user gives 2 arguments'''
        print("n should be == 2", file=sys.stderr)
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
    solve_n_queens(n, 0, [])
    if solutions:
        '''Print the solutions.'''
        for solution in solutions:
            print("[", end="")
        for i, pair in enumerate(solution):
            print(pair, end="")
        if i != len(solution) - 1:
            print(", ", end="")
            print("]")
        else:
            print("No solutions found!")


if __name__ == "__main__":
    main()
