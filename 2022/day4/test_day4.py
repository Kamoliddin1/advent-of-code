import pytest

from .solution import calc_part1, calc_part2

test_data = [
    ("""
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
    """, 2),
]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part1(input_str: str, expected: int) -> None:
    assert calc_part1(input_str) == expected


test_data = [
    ("""
    2-4,6-8
    2-3,4-5
    5-7,7-9
    2-8,3-7
    6-6,4-6
    2-6,4-8
    """, 4),
]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part2(input_str: str, expected: int) -> None:
    assert calc_part2(input_str) == expected
