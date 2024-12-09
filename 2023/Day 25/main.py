# Julia Sabelli
# Advent of Code 2023
# Day 25: Snowverload

import igraph 


def get_input(day, year):
    with open(f'input.txt', 'r') as file:
        return file.read()


text = get_input(25, 2023)
lines = text.split('\n')

verts = set()
edges = set()

for line in lines:
    a, b = line.split(': ')
    bs = b.split()

    verts.add(a)
    for b in bs:
        verts.add(b)
        edges.add((a, b))

g = igraph.Graph()

for vert in verts:
    g.add_vertex(vert)

for a, b in edges:
    g.add_edge(a, b)

cut = g.mincut()

print(len(cut.partition[0]) * len(cut.partition[1]))
