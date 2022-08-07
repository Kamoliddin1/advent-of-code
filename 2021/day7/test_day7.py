import pytest
from .solution import calc_part1, calc_part2

test_data = [("""
16,1,2,0,4,2,7,1,2,14""", 37)]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part1(input_str: str, expected: int) -> None:
    assert calc_part1(input_str) == expected


test_data = [("""
16,1,2,0,4,2,7,1,2,14""", 168)]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part2(input_str: str, expected: int) -> None:
    assert calc_part2(input_str) == expected
