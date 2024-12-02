from inspect import getsourcefile
from pathlib import Path

import pytest

from src.day2.main import (
    main,
    part_two_main,
)


@pytest.fixture
def provide_test_lines() -> list[str]:
    source_path = Path(getsourcefile(main)).resolve().parent / 'README.md'
    with source_path.open("r") as file:
        example_slice = slice(22, 28)
        return [line.strip() for line in file.readlines()[example_slice]]


def test_main(provide_test_lines: list[str]) -> None:
    expected = 2
    actual = main(provide_test_lines)
    assert actual == expected


def test_part_two_main(provide_test_lines: list[str]) -> None:
    expected = 4
    actual = part_two_main(provide_test_lines)
    assert actual == expected