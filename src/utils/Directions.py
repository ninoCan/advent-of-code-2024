from enum import Enum


class Direction(Enum):
    UP = "^"
    RIGHT = ">"
    DOWN = "v"
    LEFT = "<"

    @classmethod
    def __iter__(cls):
        return iter([member.value for member in cls])

def rotate(current: Direction) -> Direction:
    match current.value:
        case Direction.UP:
            return Direction.RIGHT
        case Direction.RIGHT:
            return Direction.DOWN
        case Direction.DOWN:
            return Direction.LEFT
        case Direction.LEFT:
            return Direction.UP