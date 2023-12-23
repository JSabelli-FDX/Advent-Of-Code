# Julia Sabelli
# Advent of Code 2023
# Day 21: Step Counter | Part 1

def count_reachable_plots(input_file, steps):
    with open(input_file, 'r') as file:
        grid = [list(line.strip()) for line in file]

    # Find the starting position
    start = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                start = (i, j)
                break
        if start:
            break

    # Directions: north, south, east, west
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Initialize the 3D array
    visited = [[[0 for _ in range(steps + 1)] for _ in range(len(grid[0]))] for _ in range(len(grid))]
    visited[start[0]][start[1]][0] = 1

    # DFS
    stack = [(start, 0)]
    while stack:
        (x, y), step = stack.pop()
        if step < steps:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] in {'.', 'S'} and visited[nx][ny][step + 1] == 0:
                    stack.append(((nx, ny), step + 1))
                    visited[nx][ny][step + 1] = 1

    return sum(visited[i][j][steps] for i in range(len(grid)) for j in range(len(grid[0])))

print(count_reachable_plots('input.txt', 64))