from collections import Counter
from idlelib.configdialog import changes
from typing import Optional, Sequence

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
    def changes(seller: Seller) -> Sequence[int]:
       prices = [el for el in seller.prices]
       for i, price in enumerate(prices):
           if i == 0: continue
           yield price - prices[i]


    def get_best_sequence(self, seller: Seller) -> Counter[str]:
        history = [el for el in self.changes(seller)]
        prices = [el for el in seller.prices]
        maximum = max(seller.prices)
        return Counter[str](
            ",".join(str(el) for el in history[i - 3:i + 1])
            for i, price in enumerate(prices)
            if i > 4 and price == maximum
        )

    @property
    def optimal_sequence(self) -> list[int]:
        counter = sum([self.get_best_sequence(seller) for seller in self.sellers], Counter())
        winner = counter.most_common(1)[0][0]
        return list(map(int, winner.split(",")))

    def sell_with_sequence(self, seller: Seller, sequence: list[int]) -> int:
        history = [el for el in self.changes(seller)]
        for i, price in enumerate(seller.prices):
            if i > 4 and history[i-3:i+1] == sequence:
                return price
        return 0

    def trade_all(self):
       self.trading_seq = self.optimal_sequence
       self.sold = sum(
           self.sell_with_sequence(seller, self.trading_seq)
           for seller in self.sellers
       )
       return self.sold
