from enum import Enum

from src.utils import Point


class NumericPad(Enum):
    _A = Point(3, 2)
    _0 = Point(3, 1)
    _1 = Point(2, 0)
    _2 = Point(2, 1)
    _3 = Point(2, 2)
    _4 = Point(1, 0)
    _5 = Point(1, 1)
    _6 = Point(1, 2)
    _7 = Point(0, 0)
    _8 = Point(0, 1)
    _9 = Point(0, 2)
