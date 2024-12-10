from copy import deepcopy
from pathlib import Path
from typing import Optional, Sequence

from src.utils import flatten


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

    @staticmethod
    def as_files(block_memory: list[list[int]]) -> list[list[int]]:
        deep_copy = deepcopy(block_memory)
        file_memory, file = [], []
        for el in deep_copy:
            if el:
                if file and el[0] != file[0]:
                    file_memory.append(deepcopy(file))
                    file.clear()
                file.append(el.pop())
            else:
                if file and not file[0] == "_":
                    file_memory.append(deepcopy(file))
                    file.clear()
                file.append("_")
        if file:
            file_memory.append(deepcopy(file))
        return file_memory

    @staticmethod
    def move_file_closer(memory, file) -> list[list[int]]:
        copied_memory = deepcopy(memory)
        size, true_index = len(file), memory.index(file)
        for inode, item in enumerate(memory):
            space = len(item)
            if inode >= true_index:
                break
            if item[0] == "_" and space >= size:
                prior = copied_memory[: inode + 1]
                middle = copied_memory[inode + 1 : true_index]
                rest = copied_memory[true_index + 1 :]
                prior[inode] = memory[true_index]
                freed = [["_"] * size]
                return (
                    prior + [["_"] for _ in range(space - size)] + middle + freed + rest
                )
        return memory

    def compress_as_file(self, file_memory: list[list[int]]) -> list[int]:
        deep_copy = deepcopy(file_memory)
        for el in reversed(file_memory):
            if el[0] != "_":
                deep_copy = self.move_file_closer(deep_copy, el)
        return [el if str(el).isdigit() else 0 for el in flatten(deep_copy)]

    def second_task(self) -> int:
        file_memory = self.as_files(self.generate_block_memory(self.lines))
        compressed = self.compress_as_file(file_memory)
        return sum([index * value for index, value in enumerate(compressed)])


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
