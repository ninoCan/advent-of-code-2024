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

def test_diagonals(under_test):
    expected = sorted([
        "159", "267", "348",  # Left diagonals
        "357", "249", "168",  # Right diagonals
    ])
    actual = sorted(under_test.diagonals)
    assert actual == expected