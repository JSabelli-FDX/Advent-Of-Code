# Julia Sabelli
# Advent of Code 2023
# Day 13: Point of Incidence | Part 1

def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        above = above[:len(below)]
        below = below[:len(above)]

        # Check for symmetry.
        if above == below:
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
