# Julia Sabelli
# Advent of Code 2023
# Day 16: The Floor Will Be Lava | Part 1

def count_energized_tiles(filename):
    with open(filename, 'r') as file:
        grid = [list(line.strip()) for line in file]

    directions = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}  # right, down, left, up
    mirrors = {'/': {'>': '^', 'v': '<', '<': 'v', '^': '>'}, '\\': {'>': 'v', 'v': '>', '<': '^', '^': '<'}}
    energized = set()
    beam = [(0, 0, '>')]  # (row, col, direction)
    visited = set()

    while beam:
        row, col, direction = beam.pop()
        while 0 <= row < len(grid) and 0 <= col < len(grid[0]):
            if (row, col, direction) in visited:
                break
            visited.add((row, col, direction))
            energized.add((row, col))
            if grid[row][col] == '.':
                pass
            elif grid[row][col] in '/\\':
                direction = mirrors[grid[row][col]][direction]
            elif grid[row][col] in '|-':
                if (direction in '<>' and grid[row][col] == '|') or (direction in '^v' and grid[row][col] == '-'):
                    beam.append((row, col, directions[direction][0] and '>' or '^'))
                    beam.append((row, col, directions[direction][0] and '<' or 'v'))
                    break
            row += directions[direction][0]
            col += directions[direction][1]

    return len(energized)


print(count_energized_tiles('input.txt'))
