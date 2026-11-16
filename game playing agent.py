def print_board(board):
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")

def check_winner(board):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in wins:
        if board[a] == board[b] == board[c]:
            if board[a] == "X":
                return 1
            if board[a] == "0":
                return -1
                
    if all(cell in ("X", "0") for cell in board):
        return 0
    return None

def minimax(board, is_max):
    result = check_winner(board)
    if result is not None:
        return result
        
    if is_max:
        best = float("-inf")
        for i in range(9):
            if board[i] not in ("X", "0"):
                temp = board[i]
                board[i] = "X"
                score = minimax(board, False)
                board[i] = temp
                best = max(best, score)
        return best
    else:
        best = float("inf")
        for i in range(9):
            if board[i] not in ("X", "0"):
                temp = board[i]
                board[i] = "0"
                score = minimax(board, True)
                board[i] = temp
                best = min(best, score)
        return best

def best_move(board):
    best_score = float("-inf")
    move = -1
    for i in range(9):
        if board[i] not in ("X", "0"):
            temp = board[i]
            board[i] = "X"
            score = minimax(board, False)
            board[i] = temp
            if score > best_score:
                best_score = score
                move = i
    return move

board = [str(i) for i in range(1, 10)]
print("Tic-Tac Toe: You are 0, AI is X")

while True:
    print_board(board)
    # AI move
    move = best_move(board)
    board[move] = "X"
    print("\nAI played:")
    print_board(board)
    
    result = check_winner(board)
    if result is not None:
        break
        
    # Human move
    while True:
        try:
            pos = int(input("Enter position (1-9): ")) - 1
            if pos < 0 or pos > 8 or board[pos] in ("X", "0"):
                print("Invalid move! Try again.")
                continue
            board[pos] = "0"
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    result = check_winner(board)
    if result is not None:
        break

print("\nFinal Board:")
print_board(board)
if result == 1:
    print("AI wins!")
elif result == -1:
    print("You win!")
else:
    print("Match Draw!")
