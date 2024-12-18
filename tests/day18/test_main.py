"""This is a template file do not use it directly."""

from inspect import getsourcefile
from pathlib import Path

import pytest

from src.day18.main import Solution, MemoryMap


@pytest.fixture
def provide_test_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / "README.md"
    with source_path.open("r") as file:
        example_slice = slice(25, 50)
        return [line.strip() for line in file.readlines()[example_slice]]


@pytest.fixture
def provide_test_map() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / "README.md"
    with source_path.open("r") as file:
        example_slice = slice(72, 79)
        return [line.strip() for line in file.readlines()[example_slice]]


def test_hurdle_map_generation(provide_test_lines, provide_test_map):
    under_test = MemoryMap(provide_test_lines, 7, 7)
    expected = provide_test_map
    actual = ["".join(row) for row in under_test.generate_memory_faults(12).data]
    assert actual == expected


def test_first_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 22
    actual = under_test.first_task()
    assert actual == expected


def test_second_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = "placeholder"
    actual = under_test.second_task()
    assert actual == expected
