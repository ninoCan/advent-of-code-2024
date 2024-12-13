import re
from collections import deque, Counter
from pathlib import Path
from typing import Optional

from numpy.random.mtrand import Sequence

from src.utils import Grid, Point


class GridWithAreas(Grid):
    BOUNDARY_PATTERN = re.compile(r"(?=(.)(?!\1))")

    def __init__(self, data: Sequence[str]):
        super().__init__(data)

    @property
    def horizontal_hedges(self) -> list[Sequence[int]]:
        row_boundaries = [deque([0]) for _ in self.rows]
        _append_boundaries_to_deque = [
            row_boundaries[idx].appendleft(match.end())
            for idx, row in enumerate(self.rows)
            for match in self.BOUNDARY_PATTERN.finditer(row)
        ]
        return row_boundaries

    @property
    def vertical_hedges(self) -> list[Sequence[int]]:
        col_boundaries: list[deque[int]] = [deque([0]) for _ in self.columns]
        _append_boundaries_to_deque = [
            col_boundaries[idx].appendleft(match.start())
            for idx, col in enumerate(self.columns)
            for match in self.BOUNDARY_PATTERN.finditer(col)
        ]
        return col_boundaries

    @property
    def topright_coners(self) -> set[Point]:
        return {
            Point(row_boundary, col_boundary)
            for row, row_boundaries in enumerate(self.horizontal_hedges)
            for row_boundary in row_boundaries
            for col, col_boundaries in enumerate(self.vertical_hedges)
            for col_boundary in col_boundaries
            if row == col_boundary and col == row_boundary
        }

    @property
    def perimeters_and_areas(self) -> Counter[str, int]:
        land_registry = Counter[str, int]()
        # TODO: logic
        return land_registry


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path = _STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        map = GridWithAreas(self.lines)
        anchors = map.topright_coners
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
