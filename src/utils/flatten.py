from itertools import chain
from typing import Any, Sequence

def flatten(nested: Sequence[Sequence[Any]]) -> Sequence[Any]:
    return list(chain.from_iterable(nested))