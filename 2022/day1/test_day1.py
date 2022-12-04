import pytest

from .solution import calc_part1, calc_part2

test_data = [
    ("""
    1000
    2000
    3000
    
    4000
    
    5000
    6000
    
    7000
    8000
    9000
    
    10000
    """, 24000),
]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part1(input_str: str, expected: int) -> None:
    assert calc_part1(input_str) == expected


test_data = [
    ("""
    1000
    2000
    3000

    4000

    5000
    6000

    7000
    8000
    9000

    10000
    """, 45000),
]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part2(input_str: str, expected: int) -> None:
    assert calc_part2(input_str) == expected
