import re
from pathlib import Path
from typing import Optional, Sequence

from src.utils import flatten, apply_n_times


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path = _STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def blink_stones(self, stones: Sequence[str]) -> Sequence[str]:
        return flatten([self.evolve_stone(stone) for stone in stones])

    @staticmethod
    def evolve_stone(stone: str) -> list[str]:
        match stone:
            case "0":
                return ["1  "]
            case s if len(s) % 2 == 0:
                middle = len(s) // 2
                return [str(int(s[middle:])), str(int(s[:middle]))]
            case s:
                return [str(int(s) * 2024)]

    def first_task(self) -> int:
        pattern = re.compile(r"\d+")
        initial_stones = pattern.findall(self.lines[0])
        return len(apply_n_times(25, self.blink_stones, initial_stones))

    def second_task(self) -> int:
        pattern = re.compile(r"\d+")
        initial_stones = pattern.findall(self.lines[0])
        return len(apply_n_times(75, self.blink_stones, initial_stones))


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
