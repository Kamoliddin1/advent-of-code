import pytest
from .solution import calc_part1

test_data = [(
    """
    2199943210
    3987894921
    9856789892
    8767896789
    9899965678
    """, 15)]


@pytest.mark.parametrize("input_str, expected", test_data)
def test_part1(input_str: str, expected: int) -> None:
    assert calc_part1(input_str) == expected
