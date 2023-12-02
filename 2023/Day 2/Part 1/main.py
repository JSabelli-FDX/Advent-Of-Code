# Julia Sabelli
# Advent of Code 2023
# Day 2: Cube Conundrum | Part 1
import re


def sum_games(doc):
    total_cubes = {'red': 12, 'green': 13, 'blue': 14}
    sum_of_ids = 0
    pattern = re.compile(r'(\d+) (\w+)')

    for line in doc:
        game_id, *games = line.split(':')
        game_id = int(game_id.split()[1])  # Extract the game ID

        for game in games:
            cubes = game.split(';')
            if any(int(num) > total_cubes[color] for cube in cubes for num, color in pattern.findall(cube)):
                break
        else:
            sum_of_ids += game_id

    return sum_of_ids


class Main:
    if __name__ == '__main__':
        with open('input.txt', 'r') as f:
            doc = [line.strip() for line in f]

        print(sum_games(doc))
