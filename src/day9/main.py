from pathlib import Path
from typing import Optional, Sequence


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def generate_block_memory(self, representation: Sequence[str]) -> list[list[int]]:
        pass

    def first_task(self) -> int:
        block_memory = self.generate_block_memory(self.lines)
        compressed_memory = self.compress(block_memory)
        return sum([index * value for index, value in enumerate(compressed_memory)])


    def second_task(self) -> int:
        pass

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()