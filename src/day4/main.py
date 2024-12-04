import re
from pathlib import Path
from typing import Optional

from src.utils import Grid, parse_all


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


    def second_task(self) -> int:
        pass

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()