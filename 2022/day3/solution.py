from pathlib import Path
from typing import List
import string
from collections import Counter

INPUTS_FILE = Path(__file__).parent / 'input.txt'


def parse(input_str: str) -> List[str]:
    lines = [s.strip() for s in input_str.split() if s.strip()]
    return lines


def make_table():
    my_table = dict()
    letters = string.ascii_letters
    for index, char in enumerate(letters, start=1):
        my_table[char] = index
    return my_table


def calc_part1(input_str) -> int:
    t = make_table()
    data = parse(input_str)
    total_item = []
    for rucksack in data:
        partition = len(rucksack) // 2
        p1 = rucksack[:partition]
        p2 = rucksack[partition:]
        items = set()
        for char in p1:
            if char in p2:
                items.add(t[char])
        total_item.append(sum(items))
    return sum(total_item)


def calc_part2(input_str) -> int:
    t = make_table()
    total = 0
    data = parse(input_str)
    repr_group = []
    n = 3
    for i in range(0, len(data), n):
        local_repr = data[i:i + n]
        a = set(local_repr[0])
        b = set(local_repr[1])
        c = set(local_repr[2])
        repr_group.append(*a.intersection(b, c))
    for i in repr_group:
        total += t[i]
    return total


def main():
    with INPUTS_FILE.open() as fp:
        input_str = fp.read()
        print(calc_part1(input_str))
        print(calc_part2(input_str))


if __name__ == "__main__":
    main()
