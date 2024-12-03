import re
from functools import reduce
from pathlib import Path
from typing import Optional

from src.utils import  flatten, parse_all

type Multiplicands = tuple[str, str]

class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    @staticmethod
    def extract_multiplicands(line: str, pattern: re.Pattern[str]) -> list[int]:
        return pattern.findall(line)

    @staticmethod
    def extract_multiplied(line: str, pattern: re.Pattern[str]) -> list[int]:
        match = pattern.findall(line)
        mul = lambda x, y: x * y
        return [reduce(mul, map(int, couple)) for couple in match]

    def first_task(self) -> int:
        pattern = re.compile(r"mul\((\d+),(\d+)\)")
        all_multiplied = flatten(parse_all(self.lines, self.extract_multiplied, pattern))
        return sum(all_multiplied)



    def second_task(self) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())