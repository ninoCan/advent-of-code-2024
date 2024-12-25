from functools import cached_property, partial

from src.day24.lazy_evaluator import LazyEvaluator


class FullAdderDebugger(LazyEvaluator):
    def __init__(self, data: list[str]):
        super().__init__(data)
        empty_line_index = data.index('\n')
        self.bugged_rules = set(row.strip("=\n") for row in data[empty_line_index + 1:])
        self.wrong_gates = set()
        self.indexed_gates = self._index_gates()

    def _index_gates(self) -> dict[str, str]:
        gates = {**{
            f"x{i:02}": f"x{i:02}"
            for i in range(self.proper_length)
        }, **{
            f"y{i:02}": f"y{i:02}"
            for i in range(self.proper_length)
        }}
        re_map = partial(self._add_new_map, gates)
        re_map("c01", {"x00", "AND", "y00"})
        re_map("z00", {"x00", "XOR", "y00"})
        for index in range(1, self.proper_length):
            i, j = f"{index:02}", f"{index + 1:02}"
            xi, yi, zi = f"x{i}", f"y{i}", f"z{i}"
            si, ci, ai, bi = f"s{i}", f"c{i}", f"a{i}", f"b{i}"
            cj = f"c{j}"
            re_map(ai, {xi, "AND", yi})
            re_map(si, {xi, "XOR", yi})
            re_map(bi, {gates[ci], "AND", gates[si]})
            re_map(zi, {gates[ci], "XOR", gates[si]})
            re_map(cj, {gates[ai], "OR", gates[bi]})
            if gates[zi] == "Missing":
                self.wrong_gates.add(gates[si])
                self.wrong_gates.add(gates[ai])
                re_map(si, {xi, "AND", yi})
                re_map(ai, {xi, "XOR", yi})
                re_map(bi, {gates[ci], "AND", gates[si]})
                re_map(zi, {gates[ci], "XOR", gates[si]})
                re_map(cj, {gates[ai], "OR", gates[bi]})
            elif gates[zi] != zi:
                self.wrong_gates.add(gates[zi])
                wrong_key = [key for key, val in gates.items() if val == zi][0]
                self.wrong_gates.add(gates[wrong_key])
                gates[zi], gates[wrong_key] = gates[wrong_key], gates[zi]
            if gates[cj] == "Missing":
                gates.pop(cj)
                re_map(cj, {gates[ai], "OR", gates[bi]})
        gates["z45"] = gates.pop("c45")
        return gates

    @cached_property
    def proper_length(self) -> int:
        initial_x = self.initial_number("x")
        initial_y = self.initial_number("y")
        proper_sum = bin(initial_x + initial_y)[2:]
        return len(proper_sum) - 1

    def _add_new_map( self, rules: dict[str], label: str, words: set[str] ):
        rules[label] = self.select(words)
        return rules

    def select(self, words: set[str]) -> str:
        rule = [el for el in self.bugged_rules if self.containing(el, words)]
        if rule:
            return rule[0].split(" ")[4]
        return f"Missing"

