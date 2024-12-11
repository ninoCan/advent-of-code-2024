from functools import reduce
from typing import Callable


def apply_n_times[T](times: int, function: Callable[[T], T], arguments: T) -> T:
    return reduce(lambda x, _: function(x), range(times), arguments)
