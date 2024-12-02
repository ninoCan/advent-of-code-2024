import re
from itertools import pairwise
from pathlib import Path

from src.utils import parse_all

type Level = list[int]

def extract_pattern(line: str, pattern: re.Pattern[str]) -> Level:
   assert pattern # ignore usage for now
   return [int(item) for item in line.split(" ")]


def is_safe(level: Level) -> bool:
    deltas = [int(right) - int(left) for left, right in pairwise(level)]
    if level[0] < level[1]:
        is_valid = lambda x: x >= 1 and x <= 3
        return all([is_valid(item) for item in deltas])
    is_valid = lambda x: x >= -3 and x <= -1
    return all([is_valid(item) for item in deltas])

def main(input_lines: list[str]) -> int:
    pattern = re.compile(r"\d+")
    all_levels = parse_all(input_lines, extract_pattern, pattern)
    safety_results = [is_safe(level) for level in all_levels]
    return safety_results.count(True)

def part_two_main(input_lines: list[str]) -> int:
    pass


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    first_answer = main(lines)
    print("The first answer is", first_answer)
    second_answer = part_two_main(lines)
    print("The second answer is", second_answer)