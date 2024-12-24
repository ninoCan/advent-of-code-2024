from pathlib import Path
from typing import Optional

from src.day24.lazy_evaluator import LazyEvaluator


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path = _STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        evaluator = LazyEvaluator(self.lines)
        return evaluator.final_number

    def second_task(self) -> str:
        pass

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
