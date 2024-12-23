from pathlib import Path
from typing import Optional

from src.day23.network_table import NetworkTable


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path=_STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> int:
        connections = NetworkTable(self.lines)
        parties = connections.lan_parties
        return sum([
            any([player.startswith("t") for player in game.split(",")])
            for game in parties
        ])


    def second_task(self) -> str:
        connections = NetworkTable(self.lines)
        clusters = connections.party_clusters
        return max(clusters, key=len)

def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())

if __name__ == "__main__":
    main()