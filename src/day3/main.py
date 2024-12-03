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
    def extract_multiplied(line: str, pattern: re.Pattern[str]) -> list[int]:
        match = pattern.findall(line)
        mul = lambda x, y: x * y
        return [reduce(mul, map(int, couple)) for couple in match]

    def first_task(self) -> int:
        pattern = re.compile(r"mul\((\d+),(\d+)\)")
        all_multiplied = flatten(parse_all(self.lines, self.extract_multiplied, pattern))
        return sum(all_multiplied)


    def _clean_input(self):
        joined_line = reduce(str.__add__, self.lines, '')
        dont_positions = [m.start() for m in re.finditer(r"don't\(\)", joined_line)]
        do_positions = [m.end() for m in re.finditer(r"do\(\)", joined_line)]
        active_strings = []
        from_index = 0
        for dont_index in dont_positions:
            active_strings.append(joined_line[from_index:dont_index])
            from_index = next(
                (do_index for do_index in do_positions if do_index > dont_index),
                len(joined_line)
            )
        return "".join(active_strings)


    def second_task(self) -> int:
        lines = [self._clean_input()]
        pattern = re.compile(r"mul\((\d+),(\d+)\)")
        all_multiplied = flatten(parse_all(lines, self.extract_multiplied, pattern))
        return sum(all_multiplied)


if __name__ == "__main__":
    solution = Solution()
    print("The first answer is", solution.first_task())
    # The first answer is 187833789
    print("The second answer is", solution.second_task())
    # The second answer is 94455185
