import heapq

goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def h(s):
    return sum(
        abs(i // 3 - (x - 1) // 3) + abs(i % 3 - (x - 1) % 3)
        for i, x in enumerate(s) if x
    )

def moves(s):
    p = s.index(0)
    r, c = divmod(p, 3)
    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            q = nr * 3 + nc
            a = list(s)
            a[p], a[q] = a[q], a[p]
            yield tuple(a)

def astar(start):
    q = [(h(start), 0, start, [start])]
    visited = set()
    while q:
        t, g, s, path = heapq.heappop(q)
        if s == goal:
            return path
        if s in visited:
            continue
        visited.add(s)
        for n in moves(s):
            if n not in visited:
                heapq.heappush(q, (g + 1 + h(n), g + 1, n, path + [n]))

start = tuple(map(int, input("Enter 9 values (0 for blank): ").split()))
path = astar(start)
if path:
    for i, s in enumerate(path):
        print(f"Step {i}")
        for j in range(0, 9, 3):
            print(s[j:j+3])
else:
    print("No solution")
