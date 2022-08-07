from typing import List
from pathlib import Path
INPUT = Path(__file__).parent / 'input.txt'


def parse(input_str: str) -> List[int]:
    return [int(i) for i in input_str.split(',') if i.strip()]


def middle_of(parsed):
    length = len(parsed)
    if length % 2 != 0:
        middle = length // 2
    else:
        p_middle = length // 2 - 1
        n_middle = length // 2
        middle = min(p_middle, n_middle)
    return middle


def calc_part1(input_str):
    parsed = sorted(parse(input_str))
    middle_elem = middle_of(parsed)
    sum_ = 0
    for elem in range(len(parsed)):
        sum_ += abs(parsed[elem] - parsed[middle_elem])
    return sum_


def calc_part2(input_str):
    crabs = parse(input_str)
    full_cost = []
    for pos in range(max(crabs)):
        cost = 0
        for crab in crabs:
            n = abs(crab - pos)
            path = (n * (n+1)) // 2
            cost += path
        full_cost.append(cost)
    return min(full_cost)


def main():
    with open(INPUT) as fp:
        input_str = fp.read()
        print(calc_part1(input_str))
        print(calc_part2(input_str))


if __name__ == '__main__':
    main()
