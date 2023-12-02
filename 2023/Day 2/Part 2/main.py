# Julia Sabelli
# Advent of Code 2023
# Day 2: Cube Conundrum | Part 2
import re


def sum_games(doc):
    sum_of_powers = 0
    pattern = re.compile(r'(\d+) (\w+)')

    for line in doc:
        game_id, *games = line.split(':')
        game_id = int(game_id.split()[1])  # Extract the game ID
        min_cubes = {'red': 0, 'green': 0, 'blue': 0}

        for game in games:
            cubes = game.split(';')
            for cube in cubes:
                matches = pattern.findall(cube)
                for match in matches:
                    num, color = match
                    min_cubes[color] = max(min_cubes[color], int(num))

        power = min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
        sum_of_powers += power

    return sum_of_powers


class Main:
    if __name__ == '__main__':
        with open('input.txt', 'r') as f:
            doc = [line.strip() for line in f]

        print(sum_games(doc))
