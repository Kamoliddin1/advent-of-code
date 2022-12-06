from pathlib import Path
from typing import Any

INPUTS_FILE = Path(__file__).parent / 'input.txt'


class Stack:
    def __init__(self):
        self.stack = []

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def get_stack(self):
        stack = ''
        for i in reversed(range(0, len(self.stack), 1)):
            stack += f"[{self.stack[i]}]\n"
        return stack

    def reverse(self):
        self.stack = self.stack[::-1]

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def crate_mover9001_pop(self, n):
        s = ''
        for _ in range(n):
            s += self.pop()
        return s[::-1]

    def crate_mover9001_push(self, popped_9001):
        for i in popped_9001:
            self.push(i)


def parse(input_str: str, N) -> tuple[dict[int, Stack], list[tuple[Any, Any, Any]]]:
    parts = input_str.split('\n\n')
    docker = parts[0].splitlines()
    instructions = []
    stacks = {}
    for i in range(N):
        s = Stack()
        stacks[i + 1] = s
    for i in range(len(docker) - 1):
        crates = docker[i][1::4]
        for j, cr in enumerate(crates, start=1):
            if cr != " ":
                stacks[j].push(cr)

    for i in range(len(stacks)):
        stacks[i + 1].reverse()

    for i in parts[1].splitlines():
        move = i.split()
        n, from_, to_ = map(int, [move[1], move[3], move[5]])
        instructions.append((n, from_, to_))
    return stacks, instructions


def calc_part1(input_str, N) -> str:
    stacks, instructions = parse(input_str, N)
    for instruction in instructions:
        n, from_, to = instruction
        for _ in range(n):
            popped = stacks[from_].pop()
            stacks[to].push(popped)
    s = ''
    for i in stacks:
        s += stacks[i].peek()
    return s


def calc_part2(input_str, N) -> str:
    stacks, instructions = parse(input_str, N)
    for instruction in instructions:
        n, from_, to = instruction
        popped = stacks[from_].crate_mover9001_pop(n)
        stacks[to].crate_mover9001_push(popped)
    s = ''
    for i in stacks:
        s += stacks[i].peek()
    return s


def main():
    with INPUTS_FILE.open() as fp:
        input_str = fp.read()
        print(calc_part1(input_str, 9))
        print(calc_part2(input_str, 9))


if __name__ == "__main__":
    main()
