from enum import Enum
from typing import Self


class Direction(Enum):
    UP = "^"
    RIGHT = ">"
    DOWN = "v"
    LEFT = "<"

    @classmethod
    def __iter__(cls):
        return iter([member.value for member in cls])

    def rotate(self) -> Self:
        # TODO: test this refactoring works
        match self.value:
            case Direction.UP:
                return Direction.RIGHT
            case Direction.RIGHT:
                return Direction.DOWN
            case Direction.DOWN:
                return Direction.LEFT
            case Direction.LEFT:
                return Direction.UP
