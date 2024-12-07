from pathlib import Path
from typing import Optional, Self

from returns.maybe import Maybe, Some, Nothing

from src.utils import Grid, Point
from src.utils.Directions import Direction, rotate


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines


    class GuardGrid(Grid):
        TRAIL_MARK = "X"
        OBSTACLE = "#"

        def locate_guard(self) -> Maybe[tuple[Point, Direction]]:
            """ Find guard position and their direction if on board. """
            for direction in Direction:
                if len(coords:=self.locate(direction.value))>0:
                     return Some((Point(int(coords[0]), int(coords[1])), direction))
            return Nothing

        @property
        def trail(self) -> list[Point]:
            return [Point(int(coords[0]), int(coords[1])) for coords in self.locate(self.TRAIL_MARK)]

        @property
        def obstructions(self) -> list[Point]:
            return [Point(int(coords[0]), int(coords[1])) for coords in self.locate(self.OBSTACLE)]

        def walk(self, guard: Maybe[tuple[Point, Direction]]) -> Self:
            if guard.empty:
               return self
            new_grid = self.copy()
            position, direction = guard
            if self.next_position(position, direction) not in self.obstructions:
                new_grid[position] = self.TRAIL_MARK
                if self.is_inside(self.next_position(position, direction)):
                    new_grid[self.next_position(position, direction)] = direction.value
                return new_grid
            new_grid[position] = rotate(direction).value
            return new_grid

        def is_inside(self, next_position: Point) -> bool:
            if (next_position.x > 0 and
                next_position.x < self.width and
                next_position.y > 0 and
                next_position.y < self.height
            ):
                return True
            return False

    def first_task(self) -> int:
        grid = self.GuardGrid(self.lines)
        while not grid.locate_guard().empty:
            grid.walk(grid.locate_guard())
        return len(grid.trail)

    def second_task(self) -> int:
        pass

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()