import pytest
from src.utils.grid import Grid

@pytest.fixture
def under_test():
    grid_data = [
        "123",
        "456",
        "789",
    ]
    return Grid(grid_data)

def test_rows(under_test):
    expected = sorted([
        "123", "456", "789",
    ])
    actual = sorted(under_test.rows)
    assert actual == expected

def test_columns(under_test):
    expected = sorted([
        "147", "258", "369",
    ])
    actual = sorted(under_test.columns)
    assert actual == expected

def test_main_diagonal(under_test):
    expected = sorted([
        "159", "267", "348",
    ])
    actual = sorted(under_test.main_diagonals)
    assert actual == expected


def test_anti_diagonals(under_test):
    expected = sorted([
        "357", "249", "168",
    ])
    actual = sorted(under_test.anti_diagonals)
    assert actual == expected

def test_toroidal_diagonals(under_test):
    expected = sorted(under_test.main_diagonals + under_test.anti_diagonals)
    actual = sorted(under_test.toroidal_diagonals)
    assert actual == expected

def test_box_diagonals(under_test):
    expected = sorted([
        "159", "26", "7", "3", "48",
        "357", "24", "9", "1", "68",
    ])
    actual = sorted(under_test.main_diagonals)
    assert actual == expected
