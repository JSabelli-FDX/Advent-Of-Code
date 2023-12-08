# Julia Sabelli
# Advent of Code 2023
# Day 8: Haunted Wasteland | Part 2

import re, math

input = open("input.txt", 'r').read()
lines = input.split('\n')

ins = lines[0]
loc = []

m = {}

for node in lines[2:]:
    w = [i for i in re.findall(r"[0-9A-Z]+", node)]
    m[w[0]] = [w[1], w[2]]
    if w[0][2] == 'A':
        loc.append(w[0])

total = 1
for node in loc:
    r = 0
    while node[2] != 'Z':
        for i in ins:
            if i == 'R':
                node = m[node][1]
            else:
                node = m[node][0]
            r += 1

    total = math.lcm(total, r)

print(total)
