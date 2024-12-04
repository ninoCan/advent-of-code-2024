from typing import Sequence

import numpy as np

class Grid:
    def __init__(self, data: Sequence[str]):
        self.width = len(data[0])
        self.height = len(data)
        self.data = np.char.asarray([
                [letter for letter in row ]
                for row in data
            ]) if data else np.char.asarray([])

    @property
    def rows(self) -> list[str]:
        return [ "".join(row) for row in self.data ]

    @property
    def columns(self) -> list[str]:
        return [ "".join(col) for col in self.data.T ]

    @property
    def diagonals(self) -> list[str]:
        return [
            "".join(self.data.diagonal(offset))
            for offset in range(-self.width + 1, self.width)
        ] + [
            "".join(np.fliplr(self.data).diagonal(offset))
            for offset in range(-self.width + 1, self.width)
        ]

