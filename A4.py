def print_board(board):
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens_util(board, col, n):
    if col >= n:
        return True
    
    for row in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  
            if solve_nqueens_util(board, col + 1, n):
                return True
            board[row][col] = 0
    
    return False

def solve_nqueens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[0][0] = 1
    
    if not solve_nqueens_util(board, 1, n):
        print("No solution exists")
    else:
        print("Final N-Queens Solution Matrix:")
        print_board(board)

n = int(input("Enter the size of the board (N): "))
solve_nqueens(n)
