"""This is a template file do not use it directly."""

from inspect import getsourcefile
from pathlib import Path

import pytest

from src.day16.main import Solution


@pytest.fixture
def provide_first_maze_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / "README.md"
    with source_path.open("r") as file:
        example_slice = slice(19, 34)
        return [line.strip() for line in file.readlines()[example_slice]]


@pytest.fixture
def provide_second_maze_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / "README.md"
    with source_path.open("r") as file:
        example_slice = slice(78, 95)
        return [line.strip() for line in file.readlines()[example_slice]]


def test_first_task(provide_first_maze_lines, provide_second_maze_lines) -> None:
    under_test_1 = Solution(lines=provide_first_maze_lines)
    under_test_2 = Solution(lines=provide_second_maze_lines)
    expected_1 = 7036
    expected_2 = 11048
    actual_1 = under_test_1.first_task()
    actual_2 = under_test_2.first_task()
    assert actual_1 == expected_1
    assert actual_2 == expected_2


def test_second_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = "placeholder"
    actual = under_test.second_task()
    assert actual == expected
