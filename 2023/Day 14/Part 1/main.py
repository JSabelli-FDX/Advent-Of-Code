# Julia Sabelli
# Advent of Code 2023
# Day 14: Parabolic Reflector Dish | Part 1

with open('input.txt', 'r') as f:
    grid = [line.strip() for line in f]
grid = list(map("".join, zip(*grid)))
grid = ["#".join(["".join(sorted(list(group), reverse=True)) for group in row.split("#")]) for row in grid]
grid = list(map("".join, zip(*grid)))

print(sum(row.count("O") * (len(grid) - r) for r, row in enumerate(grid)))
