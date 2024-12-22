from pathlib import Path
from typing import Optional

from src.day21.directional_encoder import DirectionalEncoder
from src.day21.numeric_to_directional_converter import NumericToDirectionalConverter


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    @staticmethod
    def encode_code_instructions(code: str) -> str:
        first_robot_instructions = NumericToDirectionalConverter(code).to_direction_string
        second_robot_instructions = DirectionalEncoder(first_robot_instructions).to_direction_string
        return DirectionalEncoder(second_robot_instructions).to_direction_string

    @staticmethod
    def calculate_complexity(instruction_set: str, code: str) -> int:
        return len(instruction_set) * int(code[:-1])

    def first_task(self) -> int:
        instructions = {line.strip("\n"): self.encode_code_instructions(line.strip("\n")) for line in self.lines}
        complexities  = (self.calculate_complexity(instr, code) for code, instr in instructions.items())
        return sum(complexities)



    def second_task(self) -> int:
        pass

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()

