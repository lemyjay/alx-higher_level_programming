#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    """
    Check if it's safe to place a queen at a given position.

    Args:
        board (list): The chessboard.
        row (int): The current row.
        col (int): The current column.
        N (int): The size of the chessboard.

    Returns:
        bool: True if it's safe, False otherwise.
    """
    # Check for queens in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check for queens in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check for queens in the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, row, N, solutions):
    """
    Recursive utility function to solve the N-Queens problem using
    backtracking.

    Args:
        board (list): The chessboard.
        row (int): The current row.
        N (int): The size of the chessboard.
        solutions (list): List to store solutions.

    Returns:
        None
    """
    if row == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solve_nqueens_util(board, row + 1, N, solutions)
            board[row][col] = 0


def solve_nqueens(N):
    """
    Solve the N-Queens problem and print solutions.

    Args:
        N (str): The size of the chessboard.

    Returns:
        None
    """
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0] * N for _ in range(N)]
    solutions = []

    solve_nqueens_util(board, 0, N, solutions)

    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
        
    solve_nqueens(sys.argv[1])