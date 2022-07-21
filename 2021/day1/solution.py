from pathlib import Path
from typing import List

INPUTS_FILE = Path(__file__).parent / 'input.txt'


def parse(input_str: str) -> List[int]:
    lines = [int(s.strip()) for s in input_str.split() if s.strip()]
    return lines


def calc_part1(input_str):
    data = parse(input_str)
    return sum(second > first for first, second in zip(data, data[1:]))


def calc_part2(input_str):
    data = parse(input_str)
    sum_of_three = [sum(data[i:i+3]) for i in range(len(data)-2)]
    return sum([first < second for first, second in zip(sum_of_three, sum_of_three[1:])])


def my_part(input_str):
    data = parse(input_str)
    first: int = 0
    _next: int = 1
    _sum = 0
    while _next < len(data):
        if data[first] < data[_next]:
            _sum += 1
        first += 1
        _next += 1
    return _sum


def my_part2(input_str):
    data = parse(input_str)
    sum_of_3: List = []
    count = 0
    for datum in range(len(data)-2):
        sum_of_3.append(sum(data[datum: datum+3]))
    for first, second in zip(sum_of_3, sum_of_3[1:]):
        if second > first:
            count += 1
    print(count)


def main():
    with INPUTS_FILE.open() as fp:
        input_str = fp.read()
        print(calc_part1(input_str))
        print(calc_part2(input_str))


if __name__ == "__main__":
    main()
