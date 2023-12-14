# Julia Sabelli
# Advent of Code 2023
# Day 14: Parabolic Reflector Dish | Part 2

with open('input.txt', 'r') as f:
    grid = tuple(line.strip() for line in f)


def cycle():
    global grid
    for _ in range(4):
        grid = tuple(map("".join, zip(*grid)))
        grid = tuple(
            "#".join(["".join(sorted(tuple(group), reverse=True)) for group in row.split("#")]) for row in grid)
        grid = tuple(row[::-1] for row in grid)


seen = {grid}
array = [grid]

counter = 0

while True:
    counter += 1
    cycle()
    if grid in seen:
        break
    seen.add(grid)
    array.append(grid)

first = array.index(grid)

grid = array[(1000000000 - first) % (counter - first) + first]

print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))