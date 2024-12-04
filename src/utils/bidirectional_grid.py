from typing import Sequence


class BidirectionalGrid:
    def __init__(self, data: Sequence[str]):
        self.width = len(data[0])
        self.height = len(data)
        self.data = data

    @property
    def rows(self):
        ordinary_rows = [ "".join(row) for row in self.data]
        reversed_rows = [ "".join(reversed(row)) for row in self.data]
        return  ordinary_rows + reversed_rows

    @property
    def columns(self):
        ordinary_cols = [
            "".join([
                self.data[row_idx][column_idx]
                for row_idx in range(self.width)
            ])
            for column_idx in range(self.height)
        ]
        reversed_cols = [reversed(col) for col in ordinary_cols]
        return ordinary_cols + reversed_cols

    @property
    def diagonals(self):
        ordinary_diags = [
            "".join([
                self.data[(anchor + increment) % self.height][(anchor + increment) % self.width]
                for increment in range(self.width)
            ])
            for anchor in range(self.height)
        ]
        reversed_diags = [
            "".join([
                self.data[(anchor - increment) % self.height][(anchor - increment) % self.width]
                for increment in range(self.width)
            ])
            for anchor in range(self.height)
        ]
        return ordinary_diags + reversed_diags