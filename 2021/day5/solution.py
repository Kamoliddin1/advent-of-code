from collections import defaultdict, Counter
from pathlib import Path
from typing import List, Tuple, NamedTuple, Counter
from dataclasses import dataclass

INPUTS_FILE = Path(__file__).parent / 'input.txt'


@dataclass(frozen=True)
class Point:
    x: int
    y: int


def parse(input_str: str):
    lines = [s.strip() for s in input_str.splitlines() if s.strip()]
    points = []
    for line in lines:
        pnt_1, pnt_2 = line.split('->')
        x_1, y_1 = pnt_1.split(',')
        x_2, y_2 = pnt_2.split(',')
        pt_1 = Point(int(x_1), int(y_1))
        pt_2 = Point(int(x_2), int(y_2))
        points.append((pt_1, pt_2))
    return points


def calc_part1(input_str):
    points = parse(input_str)
    counts: Counter = Counter()
    for pt_1, pt_2 in points:

        if pt_1.x == pt_2.x:
            for y in range(min(pt_1.y, pt_2.y), max(pt_1.y, pt_2.y) + 1):
                counts[Point(pt_1.x, y)] += 1
        elif pt_1.y == pt_2.y:
            for x in range(min(pt_1.x, pt_2.x), max(pt_1.x, pt_2.x) + 1):
                counts[Point(x, pt_1.y)] += 1

    return sum(1 for count in counts.values() if count > 1)


def main() -> None:
    with INPUTS_FILE.open() as fp:
        input_str = fp.read()

        print(calc_part1(input_str))


if __name__ == "__main__":
    main()
