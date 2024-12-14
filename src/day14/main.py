import math
import os
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Optional, Self

from src.utils import Grid, Point


@dataclass
class Robot:
    position: Point
    velocity: Point
    room_size: Point

    @property
    def quadrant(self) -> int:
        mid_width = self.room_size.x // 2
        mid_height = self.room_size.y // 2
        match self.position:
            case Point(x, y) if x < mid_width and y < mid_height:
                return 1
            case Point(x, y) if x > mid_width and y < mid_height:
                return 3
            case Point(x, y) if x < mid_width and y > mid_height:
                return 2
            case Point(x, y) if x > mid_width and y > mid_height:
                return 4
            case _:
                return 0

    def move_n_seconds(self, seconds: int) -> Self:
        new_x_position = (
            self.position.x + self.velocity.x * seconds
        ) % self.room_size.x
        new_y_position = (
            self.position.y + self.velocity.y * seconds
        ) % self.room_size.y
        return Robot(
            Point(new_x_position, new_y_position), self.velocity, self.room_size
        )


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path = _STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def scan_room_for_robots(self, room_size: Point) -> list[Robot]:
        pattern = re.compile(r"-?\d+")
        parsed_lines = [
            [int(match) for match in pattern.findall(line)] for line in self.lines
        ]
        return [
            Robot(Point(line[0], line[1]), Point(line[2], line[3]), room_size)
            for line in parsed_lines
        ]

    def first_task(self) -> int:
        # robots = self.scan_room_for_robots(room_size=Point(11, 7))  # test
        robots = self.scan_room_for_robots(room_size=Point(101, 103))
        quadrants = [robot.move_n_seconds(100).quadrant for robot in robots]
        return math.prod(
            [value for key, value in Counter(quadrants).items() if key != 0]
        )

    @staticmethod
    def prompt_confirmation(iteration: int, rows: list[str]) -> int:
        command = input("Press `c` to continue, `s` to stop:")
        if command == "s":
            return iteration
        return 0

    def candidate_check(self, positions: list[Point]) -> bool:
        xes = Counter([point.x for point in positions])
        yes = Counter([point.y for point in positions])
        if (
            xfreq > 50 and yfreq > 50
            for _, xfreq in xes.most_common(1)
            for _, yfreq in yes.most_common(1)
        ):
            return True

    def second_task(self) -> int:
        robots = self.scan_room_for_robots(room_size=Point(101, 103))
        iteration = 0
        while True:
            os.system("clear")
            grid = Grid((["." * 103] * 101))
            positions = [robot.move_n_seconds(iteration).position for robot in robots]
            for robot in positions:
                grid.data[*robot] = "A"
            print(f"Interation number: {iteration}")
            _print_rows = [print(row) for row in grid.rows]
            if self.candidate_check(positions):
                # if True:
                if self.prompt_confirmation(iteration, grid.rows) != 0:
                    return iteration
            iteration += 1


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
