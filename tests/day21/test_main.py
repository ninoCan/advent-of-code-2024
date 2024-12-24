""" This is a template file do not use it directly.
"""
from inspect import getsourcefile
from pathlib import Path

import pytest

from src.day21.main import Solution
from src.day21.numeric_to_directional_converter import NumericToDirectionalConverter
from src.day21.directional_encoder import DirectionalEncoder


@pytest.fixture
def provide_test_lines() -> list[str]:
    source_path = Path(getsourcefile(Solution)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(116, 121)
        return [line.strip() for line in file.readlines()[example_slice]]


def test_NumericToDirectionalConverter():
    code_stub = "029A"
    under_test = NumericToDirectionalConverter(code_stub)
    expected = "<A^A>^^AvvvA"
    actual = under_test.to_direction_string
    assert actual == expected


def test_DirectionalToDirectionalEncoder():
    instruction_stub = "<A^A>^^AvvvA"
    under_test = DirectionalEncoder(instruction_stub)
    actual = under_test.to_direction_string
    expected = "v<<A>>^A<A>AvA<^AA>A<vAAA>^A"
    # expected = "v<<A>>^A<A>AvA^<AA>Av<AAA^>A"
    assert actual == expected

def test_encode_code_instructions():
    code_stub = "029A"
    under_test = Solution
    actual = under_test.encode_code_instructions(code_stub)
    # expected = "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A"
    expected = "v<A<AA>>^AvAA^<A>Av<<A>>^AvA^Av<A^>A<Av<A>>^AAvA^Av<A<A>>^AAA<Av>A^A"
    assert actual == expected

def test_first_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = 126384
    actual = under_test.first_task()
    assert actual == expected


def test_second_task(provide_test_lines: list[str]) -> None:
    under_test = Solution(lines=provide_test_lines)
    expected = "placeholder"
    actual = under_test.second_task()
    assert actual == expected