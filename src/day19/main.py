import re
from itertools import product
from pathlib import Path
from typing import Optional

from src.day11.main import flatten


class Towels:
    def __init__(self, data: list[str]):
        pattern = re.compile(r"\w+")
        self.stripes = pattern.findall(data[0])
        self.designs = data[2:]

    def is_design_doable(self, design: str) -> bool:
        stripes_in_design = { stripe for stripe in self.stripes if stripe in design }
        print(design, ":", stripes_in_design)
        repeat = len(design) // min(len(item) for item in stripes_in_design)
        combinations = {
            "".join(els)
            for reps in range(1, repeat + 1)
            for els in product(stripes_in_design, repeat=reps) }
        if design in combinations:
            print(design)
            return True
        return False


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        towels = Towels(self.lines)
        doability_tuple = [towels.is_design_doable(design) for design in towels.designs]
        return sum(doability_tuple)

    def second_task(self) -> int:
            pass

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()