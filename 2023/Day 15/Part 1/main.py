# Julia Sabelli
# Advent of Code 2023
# Day 15: Lens Library | Part 1

def hash_algorithm(step):
    current_value = 0
    for char in step:
        ascii_value = ord(char)
        current_value += ascii_value
        current_value *= 17
        current_value %= 256
    return current_value


def sum_of_hash_results(filename):
    with open(filename, 'r') as file:
        steps = file.read().replace('\n', '').split(',')
    return sum(hash_algorithm(step) for step in steps)


print(sum_of_hash_results('input.txt'))
