import re
from typing import Callable, Optional, Sequence

def parse_all[T](
    lines: list[str],
    extract_rule: Callable[[str, re.Pattern[str]], Sequence[T]],
    pattern: Optional[re.Pattern[str]] = None,
) -> Sequence[Sequence[T]]:
    return [extract_rule(line, pattern) for line in lines]
