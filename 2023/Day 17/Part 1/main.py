# Julia Sabelli
# Advent of Code 2023
# Day 17: Clumsy Crucible | Part 1

# Open the file and read its contents
from queue import PriorityQueue

with open('input.txt', 'r') as file:
    lines = file.read().split("\n")

# The rest of the code remains the same
grid = [[int(c) for c in line] for line in lines]

result = 0

dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# (loss, state = (pos, direction, so far))
pq = PriorityQueue()
pq.put((0, ((0, 0), 0, 0)))
pq.put((0, ((0, 0), 1, 0)))
seen = set()
while not pq.empty():
    loss, state = pq.get()
    if state in seen:
        continue
    seen.add(state)
    pos, direction, so_far = state
    i, j = pos
    if i == len(grid) - 1 and j == len(grid[0]) - 1:
        result = loss
        break
    directions = [(direction + 1) % 4, (direction + 3) % 4]
    if so_far < 3:
        directions.append(direction)
    for nd in directions:
        di, dj = dir[nd]
        ni = i + di
        nj = j + dj
        if ni >= 0 and nj >= 0 and ni < len(grid) and nj < len(grid[0]):
            next_so_far = so_far + 1 if direction == nd else 1
            next_loss = loss + grid[ni][nj]
            pq.put((next_loss, ((ni, nj), nd, next_so_far)))

print(result)
