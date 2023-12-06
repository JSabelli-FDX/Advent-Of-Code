# Julia Sabelli
# Advent of Code 2023
# Day 6: Wait For It | Part 1

def calculate_ways_to_win(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        times = list(map(int, lines[0].split()[1:]))
        distances = list(map(int, lines[1].split()[1:]))

    total_ways = 1
    for time, distance in zip(times, distances):
        ways = 0
        for i in range(1, time):
            if i * (time - i) > distance:
                ways += 1
        total_ways *= ways
    return total_ways


print(calculate_ways_to_win('input.txt'))
