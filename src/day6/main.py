from pathlib import Path
from typing import Optional


from src.utils import Grid, Point
from src.utils.directions import Direction, rotate


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path = _STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    class GuardGrid(Grid):
        TRAIL_MARK = "X"
        OBSTACLE = "#"

        def locate_guard(self) -> Optional[tuple[Point, Direction]]:
            """Find guard position and their direction if on board."""
            for direction in Direction:
                if len(coords := self.locate(direction.value)) > 0:
                    return Point(int(coords[0][0]), int(coords[0][1])), direction
            return None

        @property
        def trail(self) -> list[Point]:
            return [
                Point(int(coords[0]), int(coords[1]))
                for coords in self.locate(self.TRAIL_MARK)
            ]

        @property
        def obstructions(self) -> list[Point]:
            return [
                Point(int(coords[0]), int(coords[1]))
                for coords in self.locate(self.OBSTACLE)
            ]

        @staticmethod
        def next_position(current: Point, direction: str) -> Point:
            match direction:
                case "^":
                    return Point(current.x - 1, current.y)
                case ">":
                    return Point(current.x, current.y + 1)
                case "v":
                    return Point(current.x + 1, current.y)
                case "<":
                    return Point(current.x, current.y - 1)

        def walk(self) -> None:
            if not (guard := self.locate_guard()):
                return None
            position, direction = guard
            if self.next_position(position, direction.value) not in self.obstructions:
                self.data[*position] = self.TRAIL_MARK
                next_position = self.next_position(position, direction.value)
                if self.is_inside(next_position):
                    self.data[*next_position] = direction.value
                    return None
                return None
            self.data[*position] = rotate(direction.value).value
            return None

    def first_task(self) -> int:
        grid = self.GuardGrid(self.lines)
        while grid.locate_guard():
            grid.walk()
        return len(grid.trail)

    def second_task(self) -> int:
        pass


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
