# Julia Sabelli
# Advent of Code 2023
# Day 4: Scratchcards | Part 1

lines = open('input.txt', 'r').readlines()


def calculate_points():
    total_points = 0
    for line in lines:
        winning_numbers, your_numbers = map(str.split, line.split('|'))
        matches = set(winning_numbers) & set(your_numbers)
        total_points += 2 ** (len(matches) - 1) if matches else 0
    return total_points


print(calculate_points())
