from typing import Sequence

import numpy as np

from src.utils import Point
from src.utils.Directions import Direction


class Grid:
    def __init__(self, data: Sequence[str]):
        self.width = len(data[0].strip("\n"))
        self.height = len(data)
        self.data = (
            np.char.asarray([[letter for letter in row] for row in data])
            if data
            else np.char.asarray([])
        )

    def locate(self, char: str):
        return np.argwhere(self.data == char)

    def is_inside(self, point: Point) -> bool:
        if 0 <= point.x < self.width and 0 <= point.y < self.height:
            return True
        return False

    @staticmethod
    def next_position(current: Point, direction: Direction) -> Point:
        match direction.value:
            case "^":
                return Point(current.x, current.y + 1)
            case ">":
                return Point(current.x + 1, current.y)
            case "v":
                return Point(current.x, current.y - 1)
            case "<":
                return Point(current.x - 1, current.y)

    @property
    def rows(self) -> list[str]:
        return ["".join(row) for row in self.data]

    @property
    def columns(self) -> list[str]:
        return ["".join(col) for col in self.data.T]

    @property
    def main_diagonals(self) -> list[str]:
        return [
            "".join(self.data.diagonal(offset))
            for offset in range(-self.width + 1, self.width)
        ]

    @property
    def anti_diagonals(self) -> list[str]:
        return [
            "".join(np.fliplr(self.data).diagonal(offset))
            for offset in range(-self.width + 1, self.width)
        ]

    @property
    def diagonals(self) -> list[str]:
        return self.main_diagonals + self.anti_diagonals

    def copy(self) -> "Grid":
        return Grid(self.data.copy())
