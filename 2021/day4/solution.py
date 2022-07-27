from pathlib import Path
from typing import List, Tuple

INPUTS_FILE = Path(__file__).parent / 'input.txt'


def parse(input_str: str) -> Tuple[List[List[List[int]]], List[int]]:
    lines = [s.strip() for s in input_str.split('\n') if s.strip()]
    draws = [int(s) for s in lines.pop(0).strip().split(',')]
    num_boards = len(lines) // 5

    int_lines = [[int(s) for s in line.split()] for line in lines]

    boards = []
    for i in range(num_boards):
        boards.append(int_lines[5 * i: 5 * (i + 1)])
    return boards, draws


def check_bingo(board, history) -> bool:
    for row in board:
        if all(elem in history for elem in row):
            return True
    for column in zip(*board):
        if all(elem in history for elem in column):
            return True
    return False


def sum_them(board, history) -> int:
    return sum(elem for row in board for elem in row if elem not in history)


def calc_part1(input_str: str) -> int:
    boards, draws = parse(input_str)
    for i in range(1, len(draws)):
        history = draws[:i]
        for board in boards:
            if check_bingo(board, history):
                summed = sum_them(board, history)
                return summed * history[-1]

    raise ValueError("Cannot find an answer")


def calc_part2(input_str: str) -> int:
    boards, draws = parse(input_str)

    for i in range(1, len(draws)):
        history = draws[:i]

        if len(boards) == 1 and check_bingo(boards[0], history):
            return sum_them(boards[0], history) * history[-1]

        boards = [board for board in boards if not check_bingo(board, history)]

    raise ValueError("Cannot find an answer")


def main() -> None:
    with INPUTS_FILE.open() as fp:
        input_str = fp.read()
        print(calc_part1(input_str))
        print(calc_part2(input_str))


if __name__ == "__main__":
    main()
