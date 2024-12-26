import operator
from inspect import getsourcefile
from pathlib import Path

import pytest

from src.day22.main import Solution
from src.day22.seller import Seller


@pytest.fixture
def provide_secret_number_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(65, 75)
        return [line.strip() for line in file.readlines()[example_slice]]

@pytest.fixture
def provide_test_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(81, 85)
        return [line.strip() for line in file.readlines()[example_slice]]

@pytest.fixture
def provide_second_test_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(144, 149)
        return [line.strip() for line in file.readlines()[example_slice]]




def test_secret_number(provide_secret_number_lines) -> None:
    under_test = Seller("123")
    expected = provide_secret_number_lines
    actual = [
    str(under_test.evolve(1)),
    str(under_test.evolve(2)),
    str(under_test.evolve(3)),
    str(under_test.evolve(4)),
    str(under_test.evolve(5)),
    str(under_test.evolve(6)),
    str(under_test.evolve(7)),
    str(under_test.evolve(8)),
    str(under_test.evolve(9)),
    str(under_test.evolve(10))
    ]
    assert actual == expected


def test_first_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 37327623
    actual = under_test.first_task()
    assert actual == expected


def test_second_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 23
    actual = under_test.second_task()
    assert actual == expected
