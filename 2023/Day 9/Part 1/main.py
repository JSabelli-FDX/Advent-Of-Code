# Julia Sabelli
# Advent of Code 2023
# Day 9: Mirage Maintenance | Part 1

def next_value(seq):
    all_zeroes = True
    for x in seq:
        if x != 0:
            all_zeroes = False
            break
    if all_zeroes:
        return 0
    assert (len(seq) > 1)
    history = []
    for i in range(len(seq) - 1):
        history.append(seq[i + 1] - seq[i])
    return seq[-1] + next_value(history)


result = 0

with open('input.txt', 'r') as file:  # replace 'input.txt' with your file path
    for line in file:
        line = line.strip()
        if line == "": continue
        result += next_value(list(map(int, line.split())))

print(result)
