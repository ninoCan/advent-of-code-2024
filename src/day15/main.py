from pathlib import Path
from typing import Optional

from src.day15.warehouse import Warehouse
from src.utils import Point


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path = _STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    @staticmethod
    def calculate_gps(point: Point) -> int:
        return 100 * point.x + point.y

    def first_task(self) -> int:
        initial_warehouse = Warehouse(self.lines)
        ordered_warehouse = initial_warehouse.evolve()
        return sum([self.calculate_gps(box) for box in ordered_warehouse.boxes])

    def second_task(self) -> int:
        pass


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
