from pathlib import Path
from typing import List, Tuple

INPUTS_FILE = Path(__file__).parent / 'input.txt'


def parse(input_str: str) -> List[Tuple[str, int]]:
    data = []
    for line in input_str.splitlines():
        if not line.strip():
            continue
        command, step = line.split()
        data.append((command, int(step)))
    return data


def calc_part1(input_str: str):
    data = parse(input_str)
    horizontal: int = 0
    depth: int = 0
    for command, step in data:
        if command == 'forward':
            horizontal += step
        elif command == 'down':
            depth += step
        else:
            depth -= step
    return depth * horizontal


def calc_part2(input_str: str):
    data = parse(input_str)
    horizontal, depth, aim = 0, 0, 0
    for command, step in data:
        if command == 'forward':
            horizontal += step
            depth += step * aim
        elif command == 'down':
            aim += step
        elif command == "up":
            aim -= step
        else:
            raise ValueError
    return depth * horizontal


def main():
    with INPUTS_FILE.open() as fp:
        input_str = fp.read()
        print(calc_part1(input_str))
        print(calc_part2(input_str))


if __name__ == '__main__':
    main()
