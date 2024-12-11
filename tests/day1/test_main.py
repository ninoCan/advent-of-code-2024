from inspect import getsourcefile
from pathlib import Path
from typing import List


from src.day01.main import (
    main,
    part_two_main,
)


def provide_test_lines(slc: slice) -> List[str]:
    source_path = Path(getsourcefile(main)).resolve().parent / "README.md"
    with source_path.open("r") as file:
        return [line.strip() for line in file.readlines()[slc]]


def test_main() -> None:
    expected = 11
    actual = main(provide_test_lines(slice(41, 47)))
    assert actual == expected


def test_part_two_main() -> None:
    expected = 31
    lines = provide_test_lines(slice(88, 94))
    actual = part_two_main(lines)
    assert actual == expected
