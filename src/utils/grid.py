from typing import Sequence


class Grid:
    def __init__(self, data: Sequence[str]):
        self.width = len(data[0])
        self.height = len(data)
        self.data = data

    @property
    def rows(self) -> list[str]:
        return [ "".join(row) for row in self.data]

    @property
    def columns(self) -> list[str]:
        return [
            "".join([
                self.data[row_idx][column_idx]
                for row_idx in range(self.width)
            ])
            for column_idx in range(self.height)
        ]

    @property
    def main_diagonals(self) -> list[str]:
        return [
            "".join([
                self.data[increment % self.height][(anchor + increment) % self.width]
                for increment in range(self.width)
            ])
            for anchor in range(self.height)
        ]

    @property
    def anti_diagonals(self) -> list[str]:
        return [
            "".join([
                self.data[increment % self.height][(anchor - increment) % self.width]
                for increment in range(self.width)
            ])
            for anchor in range(self.height)
        ]

    @property
    def toroidal_diagonals(self) -> list[str]:
        return self.main_diagonals + self.anti_diagonals

    @property
    def box_diagonals(self) -> list[str]:
        pass