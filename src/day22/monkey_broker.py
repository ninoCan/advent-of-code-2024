from collections import Counter
from typing import Optional

from src.day22.seller import Seller


class MonkeyBroker:
    def __init__(
            self,
            sellers: list[Seller],
            seq: Optional[tuple[int]] = None,
    ):
        self.sellers = sellers
        self.trading_seq = seq if seq else []
        self.sold = 0


    @staticmethod
    def get_best_sequences(seller: Seller) -> Counter[str]:
        changes = []
        maxes: dict[str, int] = {}
        maximum = 0
        for i, price in enumerate(seller.prices):
            if i == 0:
                maximum = price
            changes.append(price - seller.prices[i - 1])
            if price > maximum:
                maximum = price
            if i > 4 and price == maximum:
                maxes[",".join(str(el) for el in changes[-4:])] = maximum
        maxes = { key: value for key, value in maxes.items() if value == maximum}
        return Counter(maxes.keys())

    @property
    def optimal_sequence(self) -> list[int]:
        counter = Counter[str]()
        for seller in self.sellers:
            counter + self.get_best_sequences(seller)
        winner = counter.most_common(1)[0][0]
        return list(map(int, winner.split(",")))

    @staticmethod
    def sell_with_sequence(seller: Seller, sequence: list[int]) -> int:
        changes = []
        for i, price in enumerate(seller.prices):
            if i == 0: continue
            changes.append(price - seller.prices[i - 1])
            if i > 4 and changes[-4:] == sequence:
                return price
        return 0

    def trade_all(self):
       self.trading_seq = self.optimal_sequence
       self.sold = sum(
           self.sell_with_sequence(seller, self.trading_seq)
           for seller in self.sellers
       )
       return self.sold
