from pathlib import Path
from typing import List

INPUTS_FILE = Path(__file__).parent / 'input.txt'


def parse(input_str: str) -> List[int]:
    lines = [int(s) if s.strip() else 0 for s in input_str.split('\n')]
    lines.append(0)
    return lines


def calc_part1(input_str) -> int:
    data = parse(input_str)
    calories = []
    i = 0
    for colory in data:
        i += colory
        if colory == 0:
            calories.append(i)
            i = 0
    return max(calories)


def calc_part2(input_str) -> int:
    data = parse(input_str)
    calories = []
    i = 0
    for colory in data:
        i += colory
        if colory == 0:
            calories.append(i)
            i = 0
    calories.sort(reverse=True)
    return sum(calories[:3])


def main():
    with INPUTS_FILE.open() as fp:
        input_str = fp.read()
        print(calc_part1(input_str))
        print(calc_part2(input_str))


if __name__ == "__main__":
    main()
