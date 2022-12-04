import pytest

from .solution import calc_part1, calc_part2

test_data = [
    ("""
    A Y
    B X
    C Z
    """, 15),
]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part1(input_str: str, expected: int) -> None:
    assert calc_part1(input_str) == expected


test_data = [
    ("""
    A Y
    B X
    C Z
    """, 12),
]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part2(input_str: str, expected: int) -> None:
    assert calc_part2(input_str) == expected
