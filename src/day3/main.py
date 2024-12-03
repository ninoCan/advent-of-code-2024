from pathlib import Path

class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None) -> Self:
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        pass


    def second_task(self) -> int:
        pass


if __name__ == "__main__":
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task()