# Julia Sabelli
# Advent of Code 2023
# Day 6: Wait For It | Part 2

def calculate_ways_to_win(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        if not lines:
            return "The file is empty or doesn't exist"
        time = int(''.join(lines[0].split()[1:]))
        distance = int(''.join(lines[1].split()[1:]))

    ways = 0
    for i in range(1, time):
        if i * (time - i) > distance:
            ways += 1
    return ways


print(calculate_ways_to_win('input.txt'))

