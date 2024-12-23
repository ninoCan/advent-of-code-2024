from collections import defaultdict
from itertools import groupby


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

    @property
    def party_clusters(self) -> set[str]:
        grouped = defaultdict(set)
        for key, group in groupby(self.lan_parties, lambda x: x[0:2]):
            grouped[key].update(list(group))
        candidates = {
            key: { player for triple in game for player in triple.split(",")}
            for key, game in grouped.items()
            if len(game) > 1
        }
        clusters = {
            ",".join(sorted(elements)): elements for elements in candidates.values()
            if self.is_cluster(elements)
        }
        return set(clusters.keys())

    def is_cluster(self, candiate_set: set[str]) -> bool:
        connected_set = set.union(*[
            self.adjacency_table[candidate]
            for candidate in candiate_set
        ])
        for candidate in candiate_set:
            layer = { candidate }.union(self.adjacency_table[candidate])
            connected_set = connected_set.intersection(layer)
        return connected_set == candiate_set