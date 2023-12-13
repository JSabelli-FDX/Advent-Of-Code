# Julia Sabelli
# Advent of Code 2023
# Day 13: Point of Incidence | Part 2

def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        if sum(sum(0 if a == b else 1 for a, b in zip(x, y)) for x, y in zip(above, below)) == 1:
            return r

    return 0


total = 0

for block in open('input.txt').read().split("\n\n"):
    # Split grid into blocks.
    grid = block.splitlines()

    # Check for horizontal reflections in each block. If found, multiply by 100 and add to total.
    row = find_mirror(grid)
    total += row * 100

    # Check for vertical reflections in each transposed block. If found, add to total.
    col = find_mirror(list(zip(*grid)))
    total += col

print(total)
