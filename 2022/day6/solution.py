from pathlib import Path

INPUTS_FILE = Path(__file__).parent / 'input.txt'


def parse(input_str: str) -> str:
    return input_str.strip()


def sliding_window(streams, k):
    i, j = 0, k
    flag = True
    total = 0
    while flag:
        unique_stream = streams[i:j]
        first_marker = set(unique_stream)
        if len(first_marker) == k:
            flag = False
        total = i
        j += 1
        i += 1
    return total + k


def calc_part1(input_str, k: int = 4) -> int:
    streams = parse(input_str)
    k_4 = sliding_window(streams, k)
    return k_4


def calc_part2(input_str, k: int = 14) -> int:
    streams = parse(input_str)
    k_4 = sliding_window(streams, k)
    return k_4


def main():
    with INPUTS_FILE.open() as fp:
        input_str = fp.read()
        print(calc_part1(input_str))
        print(calc_part2(input_str))


if __name__ == "__main__":
    main()
