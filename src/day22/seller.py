from functools import lru_cache
from typing import Sequence


class Seller:
    _MULTIPLIER_1 = 64
    _DIVISOR = 32
    _MULTIPLIER_2 = 2048
    _MODULO = 16777216

    def __init__(self, line: str):
        self.initial_value = int(line)
        self.secret_number = None

    def prune(self, left: int) -> int:
        return left % self._MODULO

    @staticmethod
    def mix(left: int, right: int) -> int:
        return left ^ right

    def evolve(self, n_times: int = 1) -> int:
        self.secret_number = self.initial_value
        for _ in range(n_times):
            self.secret_number = self.new_secret_number(self.secret_number)
        return self.secret_number

    @lru_cache(maxsize=4000)
    def new_secret_number(self, old: int) -> int:
        multiplied = old * self._MULTIPLIER_1
        stage_1 = self.prune(self.mix(self.secret_number, multiplied))
        divided = stage_1 // self._DIVISOR
        stage_2 = self.prune(self.mix(stage_1, divided))
        final_step = stage_2 * self._MULTIPLIER_2
        return self.prune(self.mix(stage_2, final_step))

    @property
    def prices(self) -> Sequence[int]:
        for i in range(1, 2001):
            yield int(str(self.evolve(i))[-1])
