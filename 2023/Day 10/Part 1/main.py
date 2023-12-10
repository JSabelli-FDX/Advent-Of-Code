# Julia Sabelli
# Advent of Code 2023
# Day 10: Pipe Maze | Part 1

# Open the file and read the lines
with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

grid = []
start_pos = None

i = 0
for line in lines:
    grid.append(list(line))
    if "S" in line:
        start_pos = (i, line.index("S"))
    i += 1


def has_connection(r: int, c: int, direction: str) -> bool:
    pipe = grid[r][c]
    if direction == "north":
        return pipe in "S|LJ"
    elif direction == "east":
        return pipe in "S-LF"
    elif direction == "west":
        return pipe in "S-J7"
    elif direction == "south":
        return pipe in "S|F7"


def get_neighbors(r: int, c: int):
    neighbors = []
    if r > 0 and has_connection(r, c, "north"):
        if has_connection(r - 1, c, "south"):
            neighbors.append((r - 1, c))
    if c < len(grid[0]) - 1 and has_connection(r, c, "east"):
        if has_connection(r, c + 1, "west"):
            neighbors.append((r, c + 1))
    if c > 0 and has_connection(r, c, "west"):
        if has_connection(r, c - 1, "east"):
            neighbors.append((r, c - 1))
    if r < len(grid) - 1 and has_connection(r, c, "south"):
        if has_connection(r + 1, c, "north"):
            neighbors.append((r + 1, c))
    return neighbors


result = 0

queue = [(start_pos, 0)]
visited = set()
while len(queue) > 0:
    pos, i = queue.pop(0)
    r, c = pos
    if (r, c) in visited:
        continue
    visited.add((r, c))
    result = max(result, i)
    for neighbor in get_neighbors(r, c):
        queue.append((neighbor, i + 1))

print(result)
