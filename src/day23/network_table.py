from collections import defaultdict


class NetworkTable:
    def __init__(self, data: list[str]):
        _table: dict[str, set[str]] = defaultdict(set)
        for row in data:
            left, right = row.strip("\n").split("-")
            _table[left].add(right)
            _table[right].add(left)
        self.adjacency_table = _table
        self._lan_parties: set[str] = set()

    @property
    def lan_parties(self) -> set[str]:
        if self._lan_parties:
            return self._lan_parties
        parties: set[str] = set()
        for key, conns in self.adjacency_table.items():
            for conn in conns:
                for third in self.adjacency_table[key].intersection(self.adjacency_table[conn]):
                    parties.add(",".join(sorted([key, conn, third])))
        self._lan_parties = parties
        return parties
