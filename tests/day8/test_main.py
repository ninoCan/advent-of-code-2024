"""This is a template file do not use it directly."""

from inspect import getsourcefile
from pathlib import Path

import pytest

from src.day08.main import Solution


@pytest.fixture
def provide_test_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / "README.md"
    with source_path.open("r") as file:
        example_slice = slice(17, 29)
        return [line.strip() for line in file.readlines()[example_slice]]


def test_first_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 14
    actual = under_test.first_task()
    assert actual == expected


def test_second_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 34
    actual = under_test.second_task()
    assert actual == expected
