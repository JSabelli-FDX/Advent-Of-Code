# Julia Sabelli
# Advent of Code 2023
# Day 1: Trebuchet?! | Part 1
from typing import List


def calc_total(doc: List[str]) -> int:
    total = 0

    for line in doc:
        first = next((char for char in line if char.isdigit()), '')
        last = next((char for char in reversed(line) if char.isdigit()), '')

        if first and last:
            total += int(first + last)

    return total


class Main:
    if __name__ == '__main__':
        with open('Part 1/input.txt', 'r') as f:
            doc = [line.strip() for line in f]

        print(calc_total(doc))
