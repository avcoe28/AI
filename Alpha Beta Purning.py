# Alpha-Beta Pruning Algorithm

def alpha_beta(node, depth, alpha, beta, maximizing):

    # Check Leaf Node
    if isinstance(node, int):
        print("Leaf Node:", node)
        return node

    # MAX Player
    if maximizing:

        best = float('-inf')

        for child in node:

            value = alpha_beta(
                child, depth + 1,
                alpha, beta, False
            )

            best = max(best, value)
            alpha = max(alpha, best)

            print("MAX: Alpha =", alpha, "Beta =", beta)

            # Pruning Condition
            if alpha >= beta:
                print("Branch Pruned at MAX!")
                break

        return best

    # MIN Player
    else:

        best = float('inf')

        for child in node:

            value = alpha_beta(
                child, depth + 1,
                alpha, beta, True
            )

            best = min(best, value)
            beta = min(beta, best)

            print("MIN: Alpha =", alpha, "Beta =", beta)

            # Pruning Condition
            if alpha >= beta:
                print("Branch Pruned at MIN!")
                break

        return best


# Main Program

tree = [
    [[3, 5], [6, 9]],
    [[1, 2], [0, -1]]
]

print("Alpha-Beta Pruning Algorithm")
print("----------------------------")

result = alpha_beta(
    tree,
    0,
    float('-inf'),
    float('inf'),
    True
)

print("----------------------------")
print("Optimal Value:", result)
