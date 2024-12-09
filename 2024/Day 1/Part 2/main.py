from collections import Counter


def read_input():
    with open("1.txt") as f:
        return f.read().strip()


inp = read_input()
l1, l2 = [], []
for i in inp.split("\n"):
    locs = i.split()
    l1.append(int(locs[0]))
    l2.append(int(locs[1]))

def part2():
    cnt = Counter(l2)
    res = 0
    for i in l1:
        res += cnt[i] * i
    return res


print(part2())