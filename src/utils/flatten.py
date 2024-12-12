from itertools import chain
from typing import Sequence

def flatten[T](nested: Sequence[Sequence[T]]) -> Sequence[T]:
    return list(chain.from_iterable(nested))
