from enum import Enum

from src.utils import Point


class DirectionalPad(Enum):
    _A = Point(0, 2)
    _UP = Point(0, 1)
    _LEFT = Point(1, 0)
    _DOWN = Point(1, 1)
    _RIGHT = Point(1, 2)
