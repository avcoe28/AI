from collections import deque

def valid(board, r, c, n):
    # Check row and column
    for i in range(9):
        if board[r][i] == n or board[i][c] == n:
            return False
            
    # Check 3x3 box
    x = r - r % 3
    y = c - c % 3
    for i in range(x, x + 3):
        for j in range(y, y + 3):
            if board[i][j] == n:
                return False
    return True

def bfs(board):
    q = deque([board])
    while q:
        b = q.popleft()
        # Find empty cell
        empty = None
        for i in range(9):
            for j in range(9):
                if b[i][j] == 0:
                    empty = (i, j)
                    break
            if empty:
                break
                
        # If no empty cell, solution found
        if empty is None:
            return b
            
        r, c = empty
        # Try numbers 1 to 9
        for n in range(1, 10):
            if valid(b, r, c, n):
                new = [row[:] for row in b]
                new[r][c] = n
                q.append(new)

# 0 means empty
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Print unsolved Sudoku
print("Unsolved Sudoku:")
for row in board:
    print(row)

# Solve using BFS
answer = bfs(board)

# Print solved Sudoku
print("\nSolved Sudoku:")
for row in answer:
    print(row)