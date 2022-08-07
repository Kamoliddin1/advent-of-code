from typing import List, Tuple
from pathlib import Path

INPUT = Path(__file__).parent / 'input.txt'


def parse(input_str: str) -> List[Tuple[str, str]]:
    lines = [s.strip() for s in input_str.splitlines() if s.strip()]
    to_decode = []
    for line in lines:
        code, delimiter = line.strip().split('|')
        to_decode.append((code, delimiter))
    return to_decode


def calc_part1(input_str):
    parsed = parse(input_str)
    # 1,4,7,8
    predictable_len = [2, 4, 3, 7]
    count = 0
    for code, delimiter in parsed:
        del_list = delimiter.split()
        for d in del_list:
            if len(d) in predictable_len:
                count += 1

    return count


def main():
    with open(INPUT) as fp:
        input_str = fp.read()
        print(calc_part1(input_str))


if __name__ == '__main__':
    main()

