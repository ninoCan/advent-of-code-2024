from pathlib import Path
from typing import Optional

from src.day22.monkey_broker import MonkeyBroker
from src.day22.seller import Seller


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        initial_secrets = [Seller(row.strip("\n")) for row in self.lines]
        return sum(secret.evolve(2000) for secret in initial_secrets)

    def second_task(self) -> int:
        trade_monkey = MonkeyBroker(
            [Seller(row.strip("\n")) for row in self.lines]
        )
        return trade_monkey.trade_all()

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()
