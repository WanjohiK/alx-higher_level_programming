#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.
"""

from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # loop to initialize the answer list 'a'
    for i in range(n):
        a.append([i, None])

    def already_exists(column):
        """
        check that a queen does not already exist in that column           """
        for row in range(n):
            if column == a[row][1]:
                return True
        return False

    def reject(row, column):
        """
        determines whether or not to reject the solution
        """
        if (already_exists(column)):
            return False
        i = 0
        while(i < row):
            if abs(a[i][1] - column) == abs(i - row):
                return False
            i += 1
        return True

    def clear_a(row):
        """
        clears the answers from the point of failure on
        """
        for i in range(row, n):
            a[i][1] = None

    def nqueens(row):
        """
        recursive backtracking function to find the solution
        """
        for column in range(n):
            clear_a(row)
            if reject(row, column):
                a[row][1] = column
                if (row == n - 1):  # accepts the solution
                    print(a)
                else:
                    nqueens(row + 1)
                    # moves on to next row value to continue

    # start the recursive process at row = 0
    nqueens(0)
