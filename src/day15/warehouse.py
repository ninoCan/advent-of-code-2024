from typing import Sequence, override, Self

from src.utils import Grid, Point, Direction


class Warehouse(Grid):
    _BOX_TILE = "O"
    _EMPTY_TILE = "."
    _ROBOT_TILE = "@"
    _WALL_TILE = "#"

    def __init__(self, data: Sequence[str]) -> None:
        empty_line = data.index([line for line in data if len(line) <= 1][0])
        warehouse_map, movements = data[:empty_line], data[empty_line + 1 :]
        super().__init__(warehouse_map)
        self.movements = "".join(line.strip("\n") for line in movements)

    @override
    def copy(self) -> Self:
        return Warehouse(
            ["".join(row) for row in self.data.copy()] + ["", self.movements]
        )

    @property
    def robot_position(self) -> Point:
        return Point(*[int(coord) for coord in self.locate(self._ROBOT_TILE)[0]])

    @property
    def boxes(self) -> set[Point]:
        return {
            Point(int(coords[0]), int(coords[1]))
            for coords in self.locate(self._BOX_TILE)
        }

    def determine_affected_positions(
        self,
        current_position: Point,
        direction: Direction,
    ) -> Point:
        """Keeps incrementing the next position while it finds a box"""
        next_position = self.next_position(current_position, direction)
        if self.data[*next_position] != self._BOX_TILE:
            return next_position
        return self.determine_affected_positions(next_position, direction)

    def move(self, direction: Direction) -> None:
        robot = self.robot_position
        next_position = self.determine_affected_positions(robot, direction)
        if self.data[*next_position] == self._WALL_TILE:
            return None
        self.data[*next_position] = self._BOX_TILE
        self.data[*self.next_position(robot, direction)] = self._ROBOT_TILE
        self.data[*robot] = self._EMPTY_TILE

    def evolve(self, max_moves: int = None) -> Self:
        if not max_moves:
            max_moves = len(self.movements)
        new_grid = self.copy()
        for idx, move in enumerate(self.movements):
            if idx == max_moves:
                break
            new_grid.move(Direction(move))
        return new_grid
