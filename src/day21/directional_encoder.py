from src.day21.directional_pad import DirectionalPad
from src.utils import Point, Direction


class DirectionalEncoder:
    def __init__(self, code: str):
        self.code = code

    @property
    def to_direction_string(self) -> str:
        starting_key: str = "A"
        direction_set = ""
        for char in self.code:
            direction_set += self.get_directions(starting_key, char)
            starting_key = char
        return direction_set

    @staticmethod
    def _get_dir_coords(value: str) -> Point:
        return DirectionalPad[f"_{Direction(value).name}"].value

    def get_directions(self, start: str, end: str) -> str:
        start_point = DirectionalPad._A.value if start == "A" else self._get_dir_coords(start)
        end_point = DirectionalPad._A.value if end == "A" else self._get_dir_coords(end)
        delta_x = end_point.x - start_point.x
        delta_y = end_point.y - start_point.y
        if start == Direction.LEFT.value:
            return (
                Direction.UP.value * (-delta_x) +
                Direction.RIGHT.value * delta_y +
                "A"
            )
        return (
            Direction.UP.value * (-delta_x) +
            Direction.DOWN.value * delta_x +
            Direction.LEFT.value * (-delta_y) +
            Direction.RIGHT.value * delta_y +
            "A"
        )
