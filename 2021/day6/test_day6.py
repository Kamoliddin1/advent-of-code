import pytest
from solution import calc_part1

test_data = [("""
        3,4,3,1,2
        """, 5934)]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part1(input_str: str, expected: int) -> None:
    assert calc_part1(input_str, 80) == expected
