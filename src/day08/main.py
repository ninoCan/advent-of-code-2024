from collections import Counter
from itertools import combinations
from pathlib import Path
from typing import Optional

from src.day04.main import Point
from src.utils import Grid, flatten


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path = _STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    @staticmethod
    def get_first_two_antinodes(grid: Grid, left: Point, right: Point) -> list[Point]:
        one = Point(*[2 * coord_l - coord_r for coord_l, coord_r in zip(left, right)])
        two = Point(*[2 * coord_r - coord_l for coord_l, coord_r in zip(left, right)])
        return [point for point in (one, two) if grid.is_inside(point)]

    @staticmethod
    def get_all_antinodes(grid: Grid, left: Point, right: Point) -> list[Point]:
        delta = Point(*[coord_l - coord_r for coord_l, coord_r in zip(left, right)])
        above = [Point(*right)]
        candidate_above = Point(
            *[coord_r - coord_d for coord_r, coord_d in zip(right, delta)]
        )
        while grid.is_inside(candidate_above):
            above.append(candidate_above)
            candidate_above = Point(
                *[coord_r - coord_d for coord_r, coord_d in zip(candidate_above, delta)]
            )
        below = [Point(*left)]
        candidate_below = Point(
            *[coord_l + coord_d for coord_l, coord_d in zip(left, delta)]
        )
        while grid.is_inside(candidate_below):
            below.append(candidate_below)
            candidate_below = Point(
                *[coord_l + coord_d for coord_l, coord_d in zip(candidate_below, delta)]
            )
        return above + below

    def first_task(self) -> int:
        grid = Grid(self.lines)
        antennas = {
            item: grid.locate(item)
            for item in Counter("".join(flatten(grid.data.tolist()))).keys()
            if item not in (".", "\n")
        }
        antinodes = set(
            flatten(
                [
                    self.get_first_two_antinodes(grid, *pair)
                    for frequency in antennas.keys()
                    for pair in combinations(antennas[frequency], 2)
                ]
            )
        )
        return len(antinodes)

    def second_task(self) -> int:
        grid = Grid(self.lines)
        antennas = {
            item: grid.locate(item)
            for item in Counter("".join(flatten(grid.data.tolist()))).keys()
            if item not in (".", "\n")
        }
        antinodes = set(
            flatten(
                [
                    self.get_all_antinodes(grid, *pair)
                    for frequency in antennas.keys()
                    for pair in combinations(antennas[frequency], 2)
                ]
            )
        )
        return len(antinodes)


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
