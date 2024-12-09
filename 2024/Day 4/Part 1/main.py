def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    count = 0

    def check_direction(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True

    directions = [
        (0, 1),   # right
        (1, 0),   # down
        (1, 1),   # diagonal down-right
        (1, -1),  # diagonal down-left
        (0, -1),  # left
        (-1, 0),  # up
        (-1, 1),  # diagonal up-right
        (-1, -1)  # diagonal up-left
    ]

    for r in range(rows):
        for c in range(cols):
            for dx, dy in directions:
                if check_direction(r, c, dx, dy):
                    count += 1

    return count

def data():
    with open("4.txt") as f:
        return [line.strip() for line in f]

# Example usage
grid = data()
print(count_xmas(grid))