import pytest

from .solution import calc_part1, calc_part2

test_data = [
    ("""forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2
    """, 150),
]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part1(input_str: str, expected: int) -> None:
    assert calc_part1(input_str) == expected


test_data = [
    ("""
    forward 5
    down 5
    forward 8
    up 3
    down 8
    forward 2
    """, 900),
]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part2(input_str: str, expected: int) -> None:
    assert calc_part2(input_str) == expected
