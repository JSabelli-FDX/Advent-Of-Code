# Julia Sabelli
# Advent of Code 2023
# Day 12: Hot Springs | Part 2

from collections import defaultdict


def solve(input_file):
    ans = 0
    with open(input_file, 'r') as file:
        for line in file:
            line = line.strip()

            if line == "": continue

            grid, nums = line.split()

            nums = list(map(int, nums.split(",")))
            grid = grid + "?" + grid + "?" + grid + "?" + grid + "?" + grid
            nums = nums + nums + nums + nums + nums

            sts = defaultdict(int)
            sts[(0, 0)] += 1

            for i in range(len(grid)):
                new_sts = defaultdict(int)
                poss_chars = [grid[i]]
                if grid[i] == "?":
                    poss_chars = [".", "#"]
                for k, v in sts.items():
                    sofar, idx = k
                    for ch in poss_chars:
                        if idx == len(nums):
                            if ch == ".":
                                new_sts[(sofar, idx)] += v
                        else:
                            if sofar == nums[idx]:
                                if ch == ".":
                                    new_sts[(0, idx + 1)] += v
                            else:
                                if ch == "." and sofar == 0:
                                    new_sts[(sofar, idx)] += v
                                if ch == "#":
                                    new_sts[(sofar + 1, idx)] += v
                sts = new_sts

            ans += sts[(0, len(nums))] + sts[(nums[-1], len(nums) - 1)]

    return ans


print(solve('input.txt'))
