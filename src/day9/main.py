from copy import deepcopy
from pathlib import Path
from typing import Optional, Sequence


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path = _STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    @staticmethod
    def generate_block_memory(representation: Sequence[str]) -> list[list[int]]:
        memory = []
        block_index = 0
        for idx, char in enumerate(*representation):
            if char == "\n":
                break
            block_size = int(char)
            if idx % 2 == 0:
                [memory.append([block_index]) for _ in range(block_size)]
                block_index += 1
            else:
                [memory.append([]) for _ in range(block_size)]
        return memory

    @staticmethod
    def compress(block_memory: list[list[int]]) -> list[int]:
        deep_copy = deepcopy(block_memory)
        compressed_memory = []
        for el in deep_copy:
            if el:
                compressed_memory.append(el.pop())
            else:
                while deep_copy and not deep_copy[-1]:
                    deep_copy.pop()
                compressed_memory.append(deep_copy.pop().pop()) if deep_copy else None
        return compressed_memory

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
