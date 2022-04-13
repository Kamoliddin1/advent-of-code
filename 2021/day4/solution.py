from pathlib import Path
from typing import List, Tuple

INPUTS_FILE = Path(__file__).parent / 'input.txt'
print(INPUTS_FILE)


def parse(input_str: str) -> Tuple[List[List[List[int]]], List[int]]:
    lines = [s.strip() for s in input_str.split('\n') if s.strip()]
    draws = [int(s) for s in lines.pop(0).strip().split(',')]
    num_boards = len(lines) // 5

    int_lines = [[int(s) for s in line.split()] for line in lines]

    boards = []
    for i in range(num_boards):
        boards.append(int_lines[5 * i: 5 * (i + 1)])
    return boards, draws


def main() -> None:
    with INPUTS_FILE.open() as fp:
        input_str = fp.read()
        boards, draws = parse(input_str)
        items = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        print(len(items))
        for i in range(5):
            for j in range(5):
                for k in range(5):
                    item = [items[i][j][k]]



if __name__ == "__main__":
    main()
