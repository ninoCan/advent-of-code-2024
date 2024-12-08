import re
from pathlib import Path
from typing import Optional, NamedTuple

from src.utils import Grid, parse_all, Point


class Point(NamedTuple):
   x: int
   y: int

class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines


    @staticmethod
    def count_occurences(line: str, pattern: re.Pattern[str]) -> int:
        match = pattern.findall(line)
        return len(match)

    def first_task(self) -> int:
        grid = Grid(self.lines)
        pattern = re.compile(r"(?=SAMX|XMAS)")
        row_counts = parse_all(grid.rows, self.count_occurences, pattern)
        col_counts = parse_all(grid.columns, self.count_occurences, pattern)
        diag_counts = parse_all(grid.diagonals, self.count_occurences, pattern)
        return sum(row_counts + col_counts + diag_counts)

    class GridWithX(Grid):
       def locate_xes(self, pattern:re.Pattern[str] = r"(?=SAM|MAS)") -> list[Point]:
           """ Get to the points coordinates of all the x's formed by the pattern SAM|MAS. """

           rank = self.width - 1

           def to_cartesian(offset: int, index: int, anti: bool=False) -> Point:
               """ Switch from diagonal coordinates to cartesian.

               :param offset: the offset identifying the diagonal.
               :param index:  the diagonal index of the element
               :param anti: `True` for main diagonals, `False` for anti diagonals.
               :return: `Point(x, y)` the coordinate on the grid.
               """
               if abs(offset) > rank:
                   raise ValueError(f"{offset} out or range")
               elif (index < 0) or (index > 2 * rank + 1):
                   raise  ValueError(f"{index} out of range")
               match [offset]:
                   case [0]:
                       if anti:
                           return Point( index, rank - index )
                       return Point(index, index)
                   case [x] if x > 0:
                       if anti:
                           return Point(offset + index, rank - offset - index)
                       return Point(offset + index, index)
                   case [x] if x < 0:
                       if anti:
                           return Point(index, rank - offset - index)
                       return Point(offset + index, index)

           def to_offset(index):
              return index - rank

           main_coordinate_matches = [
               to_cartesian(to_offset(idx), match.start() + 1)
               for idx, diag in enumerate(self.main_diagonals)
               for match in pattern.finditer(diag)
           ]
           anti_coordinate_matches = [
               to_cartesian(to_offset(idx), match.start() + 1, anti=True)
               for idx, diag in enumerate(self.anti_diagonals)
               for match in pattern.finditer(diag)
           ]
           return list(set(main_coordinate_matches) & set(anti_coordinate_matches))

    def second_task(self) -> int:
        grid = self.GridWithX(self.lines)
        pattern = re.compile(r"(?=SAMX|XMAS)")
        return len(grid.locate_xes(pattern=pattern))

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()