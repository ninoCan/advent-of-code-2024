import re
from pathlib import Path
from typing import Optional

from src.utils import parse_all


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path = _STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def generate_combinations(
        self, current: str, remaining_numbers: list[str], contatenation=False
    ) -> list[str]:
        if not remaining_numbers:
            return [current]
        next_number, *rest = remaining_numbers
        sum_expr = f"({current} + {next_number})"
        prod_expr = f"({current} * {next_number})"
        if contatenation:
            concat_expr = f"int(str({current}) + str({next_number}))"
            return (
                self.generate_combinations(sum_expr, rest, True)
                + self.generate_combinations(prod_expr, rest, True)
                + self.generate_combinations(concat_expr, rest, True)
            )
        return self.generate_combinations(sum_expr, rest) + self.generate_combinations(
            prod_expr, rest
        )

    def extract_valid_test_values(self, line: str, pattern: re.Pattern[str]) -> str:
        test_value, *numbers = [el for el in pattern.findall(line)]
        combos_results = [
            eval(combo) for combo in self.generate_combinations(numbers[0], numbers[1:])
        ]
        return test_value if combos_results.count(int(test_value)) else "0"

    def extract_valid_test_values_with_concat(
        self, line: str, pattern: re.Pattern[str]
    ) -> str:
        test_value, *numbers = [el for el in pattern.findall(line)]
        combos_results = [
            eval(combo)
            for combo in self.generate_combinations(numbers[0], numbers[1:], True)
        ]
        return test_value if combos_results.count(int(test_value)) else "0"

    def first_task(self) -> int:
        pattern = re.compile(r"\d+")
        valid_test_values = parse_all(
            self.lines, self.extract_valid_test_values, pattern
        )
        return sum([int("".join(test_value)) for test_value in valid_test_values])

    def second_task(self) -> int:
        pattern = re.compile(r"\d+")
        valid_test_values = parse_all(
            self.lines, self.extract_valid_test_values_with_concat, pattern
        )
        return sum([int("".join(test_value)) for test_value in valid_test_values])


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
