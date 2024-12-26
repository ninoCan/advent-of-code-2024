from collections import Counter, deque
from functools import cached_property, partial
from multiprocessing import Pool
from typing import Optional

from src.day22.seller import Seller


class MonkeyBroker:
    _POOL_SIZE = 16

    def __init__(
            self,
            sellers: list[Seller],
            seq: Optional[tuple[int]] = None,
    ):
        self.sellers = sellers
        self.trading_seq = seq if seq else []
        self.sold = None

    @staticmethod
    def get_best_sequence(seller: Seller) -> Counter[str]:
        history = deque[int](maxlen=4)
        counter = Counter[str]()
        previous = 0
        for idx, price in enumerate(seller.prices):
            if idx != 0:
                history.append(int(price - previous))
            previous = price
            if idx > 4:
                sequence = ",".join(str(el) for el in history)
                if sequence not in counter.keys():
                    counter[sequence] = price
        return counter

    @cached_property
    def optimal_sequence(self) -> list[int]:
        with Pool(self._POOL_SIZE) as pool:
            best_sequences = pool.map(self.get_best_sequence, self.sellers)
        counter = sum(best_sequences, Counter())
        winner, gained_bananas = counter.most_common(1)[0]
        self.sold = gained_bananas
        return list(map(int, winner.split(",")))


    @staticmethod
    def sell_with_sequence(sequence: list[int], seller: Seller) -> int:
        history = deque[int]([], maxlen=4)
        previous =0
        for i, price in enumerate(seller.prices):
            if i != 0:
                history.append((price - previous))
            previous = price
            if i > 4 and [el for el in history] == sequence:
                    return price
        return 0

    def trade_all(self):
        if self.sold:
            return self.sold
        self.trading_seq = self.optimal_sequence
        with Pool(self._POOL_SIZE) as pool:
            sell = partial(self.sell_with_sequence, self.trading_seq)
            gained_bananas = pool.map(sell, self.sellers)
        self.sold = sum(gained_bananas)
        return self.sold
