from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Optional

from src.day4.main import Point
from src.utils import Grid, flatten


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    @staticmethod
    def get_antinodes(grid: Grid, left: Point, right: Point) -> list[Point]:
        one = Point(*[2 * coord_l - coord_r for coord_l, coord_r in zip(left, right)])
        two = Point(*[2 * coord_r - coord_l for coord_l, coord_r in zip(left, right)])
        return [point for point in (one, two) if grid.is_inside(point)]

    def first_task(self) -> int:
        grid = Grid(self.lines)
        antennas = {
            item: grid.locate(item)
            for item in Counter("".join(flatten(grid.data.tolist()))).keys()
            if item not in (".", "\n")
        }
        antinodes = set(flatten([
            self.get_antinodes(grid, *pair)
            for frequency in antennas.keys()
            for pair in combinations(antennas[frequency], 2)
        ]))
        return len(antinodes)

    def second_task(self) -> int:
        pass

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()