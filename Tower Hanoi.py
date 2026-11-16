from collections import deque

def get_successors(state):
    successors = []
    pegs = [list(peg) for peg in state]
    for i in range(3):
        if pegs[i]:
            disk = pegs[i][-1]
            for j in range(3):
                if i != j:
                    if not pegs[j] or pegs[j][-1] > disk:
                        new_pegs = [list(peg) for peg in pegs]
                        new_pegs[i].pop()
                        new_pegs[j].append(disk)
                        new_state = tuple(tuple(peg) for peg in new_pegs)
                        successors.append((new_state, (i + 1, j + 1)))
    return successors

def tower_of_hanoi_bfs(n):
    initial = (tuple(range(n, 0, -1)), (), ())
    goal = ((), (), tuple(range(n, 0, -1)))
    queue = deque([(initial, [])])
    visited = {initial}
    
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for next_state, move in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [move]))
    return None

n = int(input("Enter number of disks: "))
solution = tower_of_hanoi_bfs(n)
print("\nSolution:")
for step, move in enumerate(solution, 1):
    print(f"Step {step}: Move disk from Peg {move[0]} to Peg {move[1]}")
print(f"\nTotal moves: {len(solution)}")