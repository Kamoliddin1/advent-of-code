from typing import Iterable
from pathlib import Path
from collections import Counter

INPUT = Path(__file__).parent / 'input.txt'


def parse(input_str: str) -> Iterable[int]:
    for i in input_str.split(','):
        if i.strip():
            yield int(i)


def calc_fish(fishes):
    fish_data: Counter = Counter()
    new_fish = 8
    new_cycle = 6
    for fish, count in fishes.items():
        if fish == 0:
            fish_data.update({new_cycle: count, new_fish: count})
        else:
            fish_data.update({fish - 1: count})
    return fish_data


def calc_part1(input_str: str, days):
    fishes = Counter(parse(input_str))
    for i in range(days):
        fishes = calc_fish(fishes)
    return sum(fishes.values())


def main():
    with open(INPUT) as fp:
        input_str = fp.read()
        print(calc_part1(input_str, 80))
        print(calc_part1(input_str, 256))


if __name__ == '__main__':
    main()
