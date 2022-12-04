from dataclasses import dataclass
from pathlib import Path
from typing import List

INPUTS_FILE = Path(__file__).parent / 'input.txt'


@dataclass(order=True)
class Point:
    x: int
    y: int


def parse(input_str: str) -> List[List]:
    lines = [s.strip() for s in input_str.splitlines() if s.strip()]
    ranges = []
    for line in lines:
        sec1, sec2 = line.split(',')
        x1, y1 = sec1.split('-')
        x2, y2 = sec2.split('-')
        pt_1 = Point(int(x1), int(y1))
        pt_2 = Point(int(x2), int(y2))
        ranges.append([pt_1, pt_2])
    return ranges


def in_range(r1, r2):
    return r1.x <= r2.x and r1.y >= r2.y or r2.x <= r1.x and r2.y >= r1.y


def calc_part1(input_str) -> int:
    data = parse(input_str)
    count = 0
    for r1, r2 in data:
        count += in_range(r1, r2)
    return count


def calc_part2(input_str) -> int:
    intervals = parse(input_str)
    new_interval = []
    for i in range(len(intervals)):
        intervals[i].sort(key=lambda p: p.x)
    for interval in intervals:
        front, rear = interval
        if rear.x <= front.y < rear.y:
            new_interval.append(interval)
        elif front.y >= rear.y:
            new_interval.append(interval)
    return len(new_interval)


def main():
    with INPUTS_FILE.open() as fp:
        input_str = fp.read()
        print(calc_part1(input_str))
        print(calc_part2(input_str))


if __name__ == "__main__":
    main()
