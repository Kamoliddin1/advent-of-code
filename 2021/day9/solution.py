from typing import List
from pathlib import Path

INPUT = Path(__file__).parent / 'input.txt'


def parse(input_str: str) -> List[List[int]]:
    return [[int(elem) for elem in row.strip()] for row in input_str.splitlines() if row.strip()]


"""
2199943210
3987894921
9856789892
8767896789
9899965678
"""


def calc_part1(input_str):
    matrix = parse(input_str)
    row = len(matrix)
    column = len(matrix[0])
    unique_indices = []
    for r in range(row):
        for c in range(column):
            adjacent_indices = []
            curr = matrix[r][c]
            if r > 0:
                adjacent_indices.append((matrix[r - 1][c]))
            if r + 1 < row:
                adjacent_indices.append((matrix[r + 1][c]))
            if c > 0:
                adjacent_indices.append((matrix[r][c - 1]))
            if c + 1 < column:
                adjacent_indices.append((matrix[r][c + 1]))

            if all(curr < elem for elem in adjacent_indices):
                curr += 1
                unique_indices.append(curr)
    return sum(unique_indices)


def main():
    with open(INPUT) as fp:
        input_str = fp.read()
        print(calc_part1(input_str))


if __name__ == '__main__':
    main()
