from typing import List
from pathlib import Path

INPUT = Path(__file__).parent / 'input.txt'
"""
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


def parse(input_str: str):
    return (s.strip() for s in input_str.splitlines() if s.strip())


def calc_part1(input_str) -> int:
    pairs = parse(input_str)
    pairs_dict: dict = {'>': '<', ']': '[', '}': '{', ')': '('}
    score_dict: dict = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score: int = 0
    for pair in pairs:
        stack = list()
        for char in pair:
            if char in pairs_dict:
                if stack and pairs_dict[char] == stack[-1]:
                    stack.pop()
                    continue
                # if can't pop then it is corrupted
                score += score_dict[char]
                break
            stack.append(char)
    return score


def calc_part2(input_str):
    pairs = parse(input_str)
    pairs_dict: dict = {'>': '<', ']': '[', '}': '{', ')': '('}
    score_dict: dict = {'(': 1, '[': 2, '{': 3, '<': 4}
    scores = list()
    stack = list()
    for pair in pairs:
        for char in pair:
            if char in pairs_dict:
                if stack and pairs_dict[char] == stack[-1]:
                    stack.pop()
                    continue
                stack = []
                break

            stack.append(char)
        else:
            score = 0
            while stack:
                top = stack.pop()
                score *= 5
                score += score_dict[top]
            scores.append(score)
    return sorted(scores)[len(scores)//2]


def main():
    with open(INPUT) as fp:
        input_str = fp.read()
        print(calc_part1(input_str))
        print(calc_part2(input_str))


if __name__ == '__main__':
    main()
