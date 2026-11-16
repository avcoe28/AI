def minimax(depth, index, is_max, values, alpha, beta):
    # Base condition: leaf node
    if depth == 3:
        return values[index]
        
    if is_max:
        best = float('-inf')
        for i in range(2):
            value = minimax(depth + 1, index * 2 + i, False, values, alpha, beta)
            best = max(best, value)
            alpha = max(alpha, best)
            # Pruning condition
            if alpha >= beta:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            value = minimax(depth + 1, index * 2 + i, True, values, alpha, beta)
            best = min(best, value)
            beta = min(beta, best)
            # Pruning condition
            if alpha >= beta:
                break
        return best

# Leaf node values
values = [3, 5, 6, 9, 1, 2, 0, -1]
# Initial values
alpha = float('-inf')
beta = float('inf')
# Find optimal value
result = minimax(0, 0, True, values, alpha, beta)
print("Optimal value:", result)