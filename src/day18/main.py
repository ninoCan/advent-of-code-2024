import re
from pathlib import Path
from typing import Optional, Self

from src.utils import Grid, Point


class MemoryMap(Grid):
    _WALL = "#"
    _EMPTY = "."

    def __init__(self, data: list[str], width: int, height: int):
        self.width, self.height = width, height
        super().__init__([self._EMPTY * self.width for _ in range(height)])
        self._data = data
        self._faults = []

    @property
    def faults(self) -> list[Point]:
        if self._faults:
            return self._faults
        pattern = re.compile(r"\d+")
        parsed_faults = []
        for line in self._data:
            coords = pattern.findall(line)
            parsed_faults.append(Point(int(coords[1]), int(coords[0])))
        return parsed_faults

    def copy(self) -> Self:
        new = MemoryMap([], self.width, self.height)
        new._faults = self.faults
        return new

    def generate_memory_faults(self, number=None) -> Self:
        new_memory = self.copy()
        faults_to_add = self.faults[:number] if number else self.faults
        for point in faults_to_add:
            new_memory.data[*point] = self._WALL
        return new_memory


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path = _STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        pass

    def second_task(self) -> int:
        pass


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
