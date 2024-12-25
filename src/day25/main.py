from itertools import groupby
from pathlib import Path
from typing import Optional

from src.utils import Grid

class Lock(Grid):
    @property
    def combo(self):
        return [col.count("#") - 1 for col in self.columns]


class Key(Grid):
    @property
    def combo(self):
        return [col.count("#") - 1  for col in self.columns]

    def does_fit(self, lock: Lock) -> bool:
        key = self.combo
        pins = lock.combo
        for idx, pin in enumerate(pins):
            if key[idx] + pin > 5:
                return False
        return True

class Schematics:
    def __init__(self, data: list[str]):
        self.keys: set[Key] = set()
        self.locks: set[Lock] = set()
        _populate = [
            self.lock_key_factory(list(chunk))
            for key, chunk in groupby(data, lambda x: x not in {"\n", ""})
        ]

    def lock_key_factory(self, data: list[str]):
        clean_data = [row.strip("\n") for row in data]
        if "#" in data[0]:
            self.locks.add(Lock(clean_data))
        elif "." in data[0]:
            self.keys.add(Key(clean_data))

    @property
    def fitting_keys(self) -> int:
        return sum(
            key.does_fit(lock)
            for lock in self.locks
            for key in self.keys
        )

class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        locks_and_keys = Schematics(self.lines)
        return locks_and_keys.fitting_keys


    def second_task(self) -> int:
        pass

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()