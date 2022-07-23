import pytest

from .solution import calc_part1, calc_part2

test_data = [
    ("""
    00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010
    """, 198),
]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part1(input_str: str, expected: int) -> None:
    assert calc_part1(input_str) == expected


test_data = [
    ("""00100
    11110
    10110
    10111
    10101
    01111
    00111
    11100
    10000
    11001
    00010
    01010""", 230),
]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part2(input_str: str, expected: int) -> None:
    assert calc_part2(input_str) == expected
