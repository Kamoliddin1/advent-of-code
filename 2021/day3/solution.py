from pathlib import Path
from collections import Counter

# 198

INPUTS_FILE = Path(__file__).parent / 'input.txt'


def most_common(bits, rating: str = '') -> str:
    zeros = bits.count('0')
    ones = bits.count('1')
    if not rating:
        if zeros > ones:
            return '0'
        return '1'
    elif rating == 'oxy':
        if zeros > ones:
            return '1'
        return '0'
    elif rating == 'co2':
        if zeros > ones:
            return '0'
        return '1'


def flip_bit(bits) -> str:
    return ''.join('1' if bit == '0' else '0' for bit in bits)


def bin_decimal(bits) -> int:
    bits = bits[::-1]
    decimal: int = 0
    for index, bit in enumerate(bits):
        decimal += pow(2, index) * int(bit)
    return decimal


def parse(input_str: str) -> str:
    data = []
    splitted = input_str.strip().split()
    for i in range(len(splitted[0])):
        bits = ''
        for j in range(len(splitted)):
            bits += splitted[j][i]
        common = most_common(bits)
        data.append(common)
    return ''.join(data)


def parse_part2(input_str: str, rating: str) -> str:
    a = input_str.strip().split()
    for i in range(len(a[0])):
        if len(a) == 1:
            return a[0]
        bits = ''
        temp_dict = {'0': [], '1': []}
        for index, val in enumerate(a):
            bits += a[index][i]
            temp_dict[str(a[index][i])].append(val)
        to_remove = temp_dict[most_common(bits, rating)]
        for eliminate in to_remove:
            a.remove(eliminate)
    return a[0]


def calc_part1(input_str) -> int:
    bits = parse(input_str)
    flipped = flip_bit(bits)
    gamma_rate = bin_decimal(bits)
    epsilon_rate = bin_decimal(flipped)
    return gamma_rate * epsilon_rate


def calc_part2(input_str: str) -> int:
    oxy = parse_part2(input_str, 'oxy')
    co2 = parse_part2(input_str, 'co2')
    oxy = bin_decimal(oxy)
    co2 = bin_decimal(co2)
    return oxy * co2


def main():
    with INPUTS_FILE.open() as fp:
        input_str = fp.read()
        print(calc_part1(input_str))
        print(calc_part2(input_str))


if __name__ == '__main__':
    main()
