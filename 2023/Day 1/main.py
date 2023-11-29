from typing import List


def calc_total(doc: List[str]) -> int:
    len1 = len(doc)
    total = 0

    for i in range(len1):
        first = ''
        last = ''

        calval = 0

        line = doc[i]
        len2 = len(line)

        for j in range(len2):
            if line[j].isnumeric() and first == '':
                first = line[j]
                break

        line = line[::-1]

        for k in range(len2):
            if line[k].isnumeric() and last == '':
                last = line[k]
                break

        calval = int(first + last)
        total += calval

    return total


class Main:
    if __name__ == '__main__':
        with open('input.txt', 'r') as f:
            doc = [line.strip() for line in f]

        print(calc_total(doc))
