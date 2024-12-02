import re
from typing import Callable, Sequence

def parse_all[T](
    lines: list[str],
    extract_rule: Callable[[str, re.Pattern[str]], Sequence[T]],
    pattern: re.Pattern[str],
) -> Sequence[Sequence[T]]:
    return [extract_rule(line, pattern) for line in lines]
