from pathlib import Path
from typing import Callable, Optional

from src.utils import Direction, Grid, Point


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"
    DIRECTIONS = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]

    def __init__(self, path: Path = _STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines
        self.map = Grid(self.lines)

    def find_trails(self, trailhead: Point) -> dict[str, Point]:
        trail_id_anchor = f"{trailhead.x:02},{trailhead.y:02}:0"
        new_trails: dict[str, Point] = {trail_id_anchor: trailhead}
        self.roam_down_the_trail(trailhead, trail_id_anchor, new_trails)
        return {
            trail_id: coords
            for trail_id, coords in new_trails.items()
            if len(trail_id) == 25
        }

    def roam_down_the_trail(
        self, position: Point, trail_id: str, candidates: dict[str, Point]
    ):
        """Update the dictionary of trail candidates. Mutable method."""
        trail_step = str(len(trail_id.split(":")[1]) // 2 + 1)
        if trail_step == 10:
            return None
        for direction in self.DIRECTIONS:
            candidate_step = self.map.next_position(position, direction)
            is_good_candidate: Callable[[Point], bool] = (  # noqa: E731
                lambda x: self.map.is_inside(x) and self.map.data[*x] == trail_step
            )
            if is_good_candidate(candidate_step):
                new_trail_id = f"{trail_id}{direction.value}{trail_step}"
                candidates.setdefault(new_trail_id, candidate_step)
                self.roam_down_the_trail(candidate_step, new_trail_id, candidates)

    # def roam_down_the_trail_imm(self, position: Point, trail_id: str, candidates: dict[str, Point]) -> dict[str, Point]:
    #     """ WIP: Update the dictionary of trail candidates. Immutable method"""
    #     is_good_candidate: Callable[[Point], bool] = (  # noqa: E731
    #         lambda x: self.map.is_inside(x) and self.map.data[*x] == trail_step
    #     )
    #     candidates[trail_id] = position
    #     trail_step = len(trail_id.split(":")[1]) + 1
    #     if trail_step > 9:
    #         return candidates
    #     return {
    #         **self.roam_down_the_trail_imm(
    #             self.map.next_position(position, direction),
    #             f"{trail_id}{direction.value}",
    #             candidates
    #         )
    #         for direction in self.DIRECTIONS
    #         if is_good_candidate(self.map.next_position(position, direction))
    #     }

    def first_task(self) -> int:
        trailheads = [[int(el) for el in coords] for coords in self.map.locate("0")]

        all_trails = [self.find_trails(Point(*trailhead)) for trailhead in trailheads]
        trail_destinations = [
            len(set(destination for destination in trails.values()))
            for trails in all_trails
        ]
        return sum(trail_destinations)

    def second_task(self) -> int:
        trailheads = [[int(el) for el in coords] for coords in self.map.locate("0")]

        all_trails = [self.find_trails(Point(*trailhead)) for trailhead in trailheads]
        return sum([len(trails) for trails in all_trails])


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
