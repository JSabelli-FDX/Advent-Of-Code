# Julia Sabelli
# Advent of Code 2023
# Day 16: The Floor Will Be Lava | Part 2

from collections import deque


class _(tuple):
    def __add__(self, other):
        return _(x + y for x, y in zip(self, other))


NORTH = _((-1, 0))
SOUTH = _((1, 0))
EAST = _((0, 1))
WEST = _((0, -1))


def do(grid, start, dstart):
    q = deque([(_(start), _(dstart))])
    visited = set()

    while q:
        i, di = q.popleft()
        if i not in grid or (i, di) in visited:
            continue
        visited.add((i, di))
        if grid[i] == "/":
            di = -di[1], -di[0]
            q.append((i + di, di))
        elif grid[i] == "\\":
            di = di[1], di[0]
            q.append((i + di, di))
        elif grid[i] == "|" and di[0] == 0:
            q.append((i + NORTH, NORTH))
            q.append((i + SOUTH, SOUTH))
        elif grid[i] == "-" and di[1] == 0:
            q.append((i + EAST, EAST))
            q.append((i + WEST, WEST))
        else:
            q.append((i + di, di))

    return len(set(p for p, _ in visited))


def p1(f):
    grid = {(i, j): x for i, row in enumerate(f) for j, x in enumerate(row.strip())}
    return do(grid, (0, 0), EAST)


def p2(f):
    lines = f.read().splitlines()
    grid = {(i, j): x for i, row in enumerate(lines) for j, x in enumerate(row)}
    n, m = len(lines), len(lines[0])

    ans = 0
    for i in range(n):
        ans = max(ans, do(grid, (0, i), SOUTH))
        ans = max(ans, do(grid, (n - 1, i), NORTH))
    for i in range(m):
        ans = max(ans, do(grid, (0, i), EAST))
        ans = max(ans, do(grid, (m - 1, i), WEST))

    return ans


print(p2(open('input.txt', 'r')))
