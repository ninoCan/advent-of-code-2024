from collections import Counter
from dataclasses import dataclass
from enum import Enum
from pathlib import Path
from typing import Optional, Self

from src.utils import Grid, Direction, Point
from src.utils.directions import rotate


@dataclass
class Trail:
    path: str

    @property
    def score(self):
        counter = Counter(self.path)
        turns_score = (counter.pop("L") + counter.pop("R")) * 1000
        return turns_score + counter.total()

    def __dict__(self) -> dict[Self, int]:
        return {self: self.score}

class Turn(Enum):
    LEFT = "L"
    FORWARD = "F"
    RIGHT = "R"


@dataclass
class Labyrinth(Grid):
    _WALL = "#"
    _END = "E"
    _movements = Turn.__members__

    def __init__(self, data: list[str]):
        super().__init__(data)
        self.orientation = Direction.RIGHT
        self.total_paths: dict[Trail, int] = {}
        self.candidate_path: dict[Trail, int] = {}

    @property
    def scout(self):
        return [Point(coords[0], coords[1]) for coords in self.locate("S")][0]

    def move(self, current: Trail, orientation) -> None:
        new_path = current.path + orientation.value
        match orientation:
            case Turn.LEFT:
                self.orientation = rotate(orientation)
                pass
            case Turn.FORWARD:
                candidate_next = self.next_position(self.scout, self.orientation)
                if self.data[*candidate_next] == self._WALL:
                    return None
                elif self.data[*candidate_next] == self._END:
                    self.total_paths.update(Trail(new_path).__dict__())
                    return None

            case Turn.RIGHT:
                pass


    def scout_path(self) -> list[Trail]:
        while self.scout:
            pass

class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        maze = Labyrinth(self.lines)
        return maze.discover_minimum_path().score

    def second_task(self) -> int:
        pass


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
