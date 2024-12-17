"""This is a template file do not use it directly."""

from inspect import getsourcefile
from pathlib import Path

import pytest

from src.day17.main import Solution, Program


@pytest.fixture
def provide_test_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / "README.md"
    with source_path.open("r") as file:
        example_slice = slice(109, 114)
        return [line.strip() for line in file.readlines()[example_slice]]


@pytest.fixture
def provide_second_test_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / "README.md"
    with source_path.open("r") as file:
        example_slice = slice(130, 135)
        return [line.strip() for line in file.readlines()[example_slice]]


def test_first_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = "4,6,3,5,6,3,5,2,1,0"
    actual = under_test.first_task()
    assert actual == expected


def test_example_1() -> None:
    under_test = Program(C=9, instructions="2,6")
    expected = 1
    _ = under_test.run()
    actual = under_test.register_B
    assert actual == expected


def test_example_2() -> None:
    under_test = Program(A=10, instructions="5,0,5,1,5,4")
    expected = "0,1,2"
    actual = under_test.run()
    assert actual == expected


def test_example_3() -> None:
    under_test = Program(A=2024, instructions="0,1,5,4,3,0")
    expected = "4,2,5,6,7,7,7,7,3,1,0"
    actual = under_test.run()
    assert actual == expected


def test_example_4() -> None:
    under_test = Program(B=29, instructions="1,7")
    expected = 26
    _ = under_test.run()
    actual = under_test.register_B
    assert actual == expected


def test_example_5() -> None:
    under_test = Program(B=2024, C=43690, instructions="4,0")
    expected = 44354
    _ = under_test.run()
    actual = under_test.register_B
    assert actual == expected


def test_second_task(provide_second_test_lines) -> None:
    under_test = Solution(lines=provide_second_test_lines)
    expected = 117440
    actual = under_test.second_task()
    assert actual == expected
