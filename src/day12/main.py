import re
from collections import deque, Counter
from pathlib import Path
from typing import Optional

from numpy.random.mtrand import Sequence

from src.utils import Grid


class GridWithAreas(Grid):
    BOUNDARY_PATTERN = re.compile(r"(?=(.)(?!\1))")

    def __init__(self, data: Sequence[str]):
        super().__init__(data)

    @property
    def horizontal_hedges(self) -> list[Sequence[int]]:
        boundaries = [deque(*self.BOUNDARY_PATTERN.finditer(row)) for row in self.rows]
        _add_left_perimeter = [row.appendleft(0) for row in boundaries]
        _add_right_perimeter = [row.append(self.width) for row in boundaries]
        return boundaries

    @property
    def vertical_hedges(self) -> list[Sequence[int]]:
        boundaries = [
            deque(*self.BOUNDARY_PATTERN.finditer(col)) for col in self.columns
        ]
        _add_left_perimeter = [col.appendleft(0) for col in boundaries]
        _add_right_perimeter = [col.append(self.height) for col in boundaries]
        return boundaries

    @property
    def perimeters_and_areas(self) -> Counter[str, int]:
        land_registry = Counter[str, int]()

        return land_registry


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path = _STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        map = GridWithAreas(self.lines)
        return sum(
            [perimeter * area for perimeter, area in map.perimeters_and_areas.items()]
        )

    def second_task(self) -> int:
        pass


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
