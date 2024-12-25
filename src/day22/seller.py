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
            multiplied = self.secret_number * self._MULTIPLIER_1
            self.secret_number = self.prune(self.mix(self.secret_number, multiplied))
            divided = self.secret_number // self._DIVISOR
            self.secret_number = self.prune(self.mix(self.secret_number, divided))
            final_step = self.secret_number * self._MULTIPLIER_2
            self.secret_number = self.prune(self.mix(self.secret_number, final_step))
        return self.secret_number

    @property
    def prices(self) -> Sequence[int]:
        return [int(str(self.evolve(i))[-1]) for i in range(1, 2001)]
