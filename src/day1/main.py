import re
from pathlib import Path
from unittest.mock import right


def extract_two_digits(line: str, pattern: re.Pattern[str]) -> tuple[int, int]:
    matching = pattern.findall(line)
    return int(matching[0][0]), int(matching[0][1])

def parse_all(lines: list[str], pattern: re.Pattern[str]) -> tuple[list[int], list[int]]:
    tuples = [extract_two_digits(line, pattern) for line in lines]
    return zip(*tuples)

def main(input_lines: list[str]) -> int:
    pattern = re.compile(r"(\d+)\s+(\d+)")
    list1, list2 = parse_all(input_lines, pattern)
    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    delta_list = [abs(b - a) for a, b in zip(sorted_list1, sorted_list2)]
    return sum(delta_list)

def part_two_main(input_lines: list[str]) -> int:
    pattern = re.compile(r"(\d+)\s+(\d+)")
    list1, list2 = parse_all(input_lines, pattern)
    left = sorted(list1)
    right = sorted(list2)
    similarity_scores = [item * right.count(item) for item in left]
    return sum(similarity_scores)


if __name__ == "__main__":
    file_path = Path(__file__).parent / "input.txt"
    with open(file_path) as file:
        lines = file.readlines()
    first_answer = main(lines)
    print("The first answer is", first_answer)
    second_answer = part_two_main(lines)
    print("The second answer is", second_answer)