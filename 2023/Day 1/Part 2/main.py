# Julia Sabelli
# Advent of Code 2023
# Day 1: Trebuchet?! | Part 2
from typing import List

from regex import regex


def calc_total(doc: List[str]) -> int:

    rx_line = [regex.findall(r"(\d|zero|one|two|three|four|five|six|seven|eight|nine)", line, overlapped=True) for line
               in doc]

    converted = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }

    num_line = [[int(n) if n.isdigit() else converted[n] for n in nums] for nums in rx_line]

    total = sum([int(calval[0] * 10 + calval[-1]) for calval in num_line])

    return total


class Main:
    if __name__ == '__main__':
        with open('input.txt', 'r') as f:
            doc = [line.strip() for line in f]

        print(calc_total(doc))
