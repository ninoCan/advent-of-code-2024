from enum import Enum


class Direction(Enum):
    UP = "^"
    RIGHT = ">"
    DOWN = "v"
    LEFT = "<"

    @classmethod
    def __iter__(cls):
        return iter([member.value for member in cls])


def rotate(current: str) -> Direction:
    match current:
        case "^":
            return Direction.RIGHT
        case ">":
            return Direction.DOWN
        case "v":
            return Direction.LEFT
        case "<":
            return Direction.UP
