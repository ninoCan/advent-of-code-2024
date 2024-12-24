from src.day21.numeric_pad import NumericPad
from src.utils import Direction


class NumericToDirectionalConverter:
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
    def get_directions(start: str, end: str) -> str:
        start_point = NumericPad[f"_{start}"].value
        end_point = NumericPad[f"_{end}"].value
        delta_x = end_point.x - start_point.x
        delta_y = end_point.y - start_point.y
        if start in ("0", "A"):
            return (
            Direction.UP.value * (-delta_x) +
            Direction.RIGHT.value * delta_y +
            Direction.LEFT.value * (-delta_y) +
            "A"
        )
        return (
            Direction.RIGHT.value * delta_y +
            Direction.LEFT.value * (-delta_y) +
            Direction.DOWN.value * delta_x +
            Direction.UP.value * (-delta_x) +
            "A"
        )
