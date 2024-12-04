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
    def diagonals(self) -> list[str]:
        main_diagonals = [
            "".join([
                self.data[(increment) % self.height][(anchor + increment) % self.width]
                for increment in range(self.width)
            ])
            for anchor in range(self.height)
        ]
        anti_diagonals = [
            "".join([
                self.data[(increment) % self.height][(anchor - increment) % self.width]
                for increment in range(self.width)
            ])
            for anchor in range(self.height)
        ]
        return main_diagonals + anti_diagonals