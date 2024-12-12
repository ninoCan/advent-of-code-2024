from collections import Counter
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
        initial_stones = self.lines[0].split()
        return len(apply_n_times(25, self.blink_stones, initial_stones))

    @staticmethod
    def count_new_stones(previous_stones: Counter[str, int]) -> Counter[str, int]:
        new_counter = Counter[str, int]()
        for stone_number, count in previous_stones.items():
            match stone_number:
                case "0":
                    new_counter.update(["1"] * count)
                case s if len(s) % 2 == 0:
                    middle = len(s) // 2
                    new_counter.update([str(int(s[middle:]))] * count)
                    new_counter.update([str(int(s[:middle]))] * count)
                case s:
                    new_counter.update([str(int(s) * 2024)] * count)
        return new_counter

    def second_task(self) -> int:
        stone_counter = Counter[str, int](self.lines[0].split())
        final_counter = apply_n_times(75, self.count_new_stones, stone_counter)
        return final_counter.total()


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
