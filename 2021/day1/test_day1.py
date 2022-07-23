import pytest

from .solution import calc_part1, calc_part2

test_data = [
    ("""
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263
    """, 7),
]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part1(input_str: str, expected: int) -> None:
    assert calc_part1(input_str) == expected


test_data = [
    ("""
    199
    200
    208
    210
    200
    207
    240
    269
    260
    263
    """, 5),
]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part2(input_str: str, expected: int) -> None:
    assert calc_part2(input_str) == expected
