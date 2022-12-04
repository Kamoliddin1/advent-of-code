from pathlib import Path
from typing import List

INPUTS_FILE = Path(__file__).parent / 'input.txt'


def parse(input_str: str) -> List[tuple[str, str]]:
    lines = []
    for line in input_str.splitlines():
        if not line.strip():
            continue
        x, y = line.split()
        lines.append((x, y))
    return lines


win_table = {
    'A': "Rock",
    'X': "Rock",
    'B': "Paper",
    'Y': "Paper",
    'C': "Scissors",
    'Z': "Scissors",
}
score_table = {
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def is_winning(elf, me) -> int:
    if me == elf:
        return 3
    elif me == "Rock":
        if elf == "Paper":
            return 0
        else:
            return 6
    elif me == "Paper":
        if elf == "Scissors":
            return 0
        else:
            return 6
    elif me == "Scissors":
        if elf == "Rock":
            return 0
        else:
            return 6


def calc_part1(input_str) -> int:
    scores = 0
    game_data = parse(input_str)
    for game in game_data:
        elf, me = game
        points = is_winning(win_table[elf], win_table[me])
        scores += points + score_table[me]
    return scores


def figure_out(me, elf) -> tuple[int, int]:
    score = None
    chose = None
    match me:
        case 'X':
            score = 0
            if elf == "Rock":
                chose = 3
            elif elf == 'Paper':
                chose = 1
            else:
                chose = 2
        case 'Y':
            if elf == "Rock":
                chose = 1
            elif elf == 'Paper':
                chose = 2
            else:
                chose = 3
            score = 3
        case 'Z':
            if elf == "Rock":
                chose = 2
            elif elf == 'Paper':
                chose = 3
            else:
                chose = 1
            score = 6
    return score, chose


def calc_part2(input_str) -> int:
    data = parse(input_str)
    scores = 0
    for game in data:
        elf, me = game
        points = figure_out(me, win_table[elf])
        scores += sum(points)
    return scores


def main():
    with INPUTS_FILE.open() as fp:
        input_str = fp.read()
        # print(calc_part1(input_str))
        print(calc_part2(input_str))


if __name__ == "__main__":
    main()
