# Julia Sabelli
# Advent of Code 2023
# Day 4: Scratchcards | Part 2

lines = open('input.txt', 'r').readlines()


def calculate_cards():
    cards = [1] * len(lines)
    for i, line in enumerate(lines):
        x, y = map(str.split, line.split('|'))
        n = len(set(x) & set(y))
        for j in range(i + 1, min(i + 1 + n, len(lines))):
            cards[j] += cards[i]
    return sum(cards)


print(calculate_cards())
