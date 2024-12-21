from collections import Counter
from pathlib import Path
from typing import Optional

import numpy as np

from src.utils import Grid, Point, Direction


class RaceTrack(Grid):
    _START = "S"
    _END = "E"
    _WALL = "#"

    def __init__(self, lines: list[str]):
        super().__init__(lines)
        self.original_path = self._capture_original_path()

    def _capture_original_path(self) -> list[Point]:
        path = list(self.locate(self._START))
        while self.data[*path[-1]] != self._END:
            last_point = path[-1]
            path.append([
                            point for point in self.nearest_neighbors(last_point)
                            if self.data[*point] != self._WALL and point not in path
                        ][0])
        return path

    @property
    def represent(self) -> np.array:
        empty_map = np.full((self.width, self.height), "  ")
        for idx, point in enumerate(self.original_path):
            empty_map[point] = str(idx)
        return empty_map

    def cheating_destinations(self, position: Point, turns=True) -> set[Point]:
        if turns:
            nns = {point for point in self.nearest_neighbors(position) if self.data[*point] == self._WALL}
            next_to_nns = set.union(*(
                self.nearest_neighbors(nn) for nn in nns
                if nn != position
            ))
            return {nnn for nnn in next_to_nns if self.data[*nnn] != self._WALL}
        straight_nnns = []
        for direction in Direction.__members__.values():
            n_n = self.next_position(position, direction)
            nnn = self.next_position(n_n, direction)
            are_inside = self.is_inside(n_n) and self.is_inside(nnn)
            if are_inside and self.data[*n_n] == self._WALL and self.data[*nnn] != self._WALL:
                straight_nnns.append(nnn)
        return set(straight_nnns)

    def long_cheat_destination(self, position: Point, max_ps=20) -> set[Point]:
        times = {point: idx for idx, point in enumerate(self.original_path)}
        walled_nns = {point for point in self.nearest_neighbors(position) if self.data[*point] == self._WALL}
        destinations = set()
        for wnn in walled_nns:
            destinations = destinations.union({
                point for point in times.keys()
                if  1 <= abs(point.x - wnn.x) + abs(point.y - wnn.y) <= max_ps - 1
                    and point != position
                    and times[point] > times[position]
            })
        return destinations

    @property
    def cheats(self) -> Counter[int, int]:
        times = {point: idx for idx, point in enumerate(self.original_path)}
        return Counter[int, int](
            times[cheat] - times[point] - 2
            for point in times.keys()
            for cheat in self.cheating_destinations(point, False)
            if times[cheat] > times[point]
        )

    def ps_20_cheats(self) -> Counter[int, int]:
        times = {point: idx for idx, point in enumerate(self.original_path)}
        return Counter[int, int](
            times[cheat] - times[point] - 2
            for point in times.keys()
            for cheat in self.long_cheat_destination(point)
            if times[cheat] > times[point]
        )


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path = _STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        race_track = RaceTrack(self.lines)
        return sum([value for key, value in race_track.cheats.items() if key >= 100])

    def second_task(self) -> int:
        pass


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
