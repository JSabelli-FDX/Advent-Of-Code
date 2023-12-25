# Julia Sabelli
# Advent of Code 2023
# Day 24: Never Tell Me The Odds | Part 2

import sympy

hailstones = [tuple(map(int, line.replace("@", ",").split(","))) for line in open('../Part 1/input.txt')]

xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr, yr, zr, vxr, vyr, vzr")

equations = []
answers = []

for i, (sx, sy, sz, vx, vy, vz) in enumerate(hailstones):
    equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
    equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
    if i < 2:
        continue
    answers = [solution for solution in sympy.solve(equations) if all(x % 1 == 0 for x in solution.values())]
    if len(answers) == 1:
        break

answer = answers[0]

print(answer[xr] + answer[yr] + answer[zr])
