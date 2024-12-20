""" This is a template file do not use it directly.
"""
from inspect import getsourcefile
from pathlib import Path

import pytest

from src.day20.main import Solution, RaceTrack


@pytest.fixture
def provide_test_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(18, 33)
        return [line.strip() for line in file.readlines()[example_slice]]


def test_cheat_counter(provide_test_lines):
    under_test = RaceTrack(provide_test_lines)
    actual = under_test.cheats
    assert actual[64] == 1
    assert actual[40] == 1
    assert actual[38] == 1
    assert actual[36] == 1
    assert actual[20] == 1
    assert actual[12] == 3
    assert actual[10] == 2
    assert actual[8] == 4
    assert actual[6] == 2
    assert actual[4] == 14
    assert actual[2] == 14


def test_first_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 0
    actual = under_test.first_task()
    assert actual == expected


def test_second_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = "placeholder"
    actual = under_test.second_task()
    assert actual == expected