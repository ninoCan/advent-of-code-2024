from collections import OrderedDict
from functools import cached_property, partial

from src.day24.lazy_evaluator import LazyEvaluator


class FullAdderDebugger(LazyEvaluator):
    def __init__(self, data: list[str]):
        super().__init__(data)
        empty_line_index = data.index('\n')
        self.wrong_rules = set(row.strip("=\n") for row in data[empty_line_index + 1:])
        self.x_and_y_gates = OrderedDict(
            (f"a{index:02}", self.select({f"x{index:02}", "AND", f"y{index:02}"}))
            for index in range(1, self.proper_length)
        )
        self.x_xor_y_gates = OrderedDict(
            (f"s{index:02}", self.select({f"x{index:02}", "XOR", f"y{index:02}"}))
            for index in range(1, self.proper_length)
        )
        self.carry_and_half_adder_gates = OrderedDict()
        self.carry_gates = OrderedDict(
            [("c01", self.select({"x00", "AND", "y00"}))]
        )
        self.find_proper_gates()

    def find_proper_gates(self):
        self.carry_and_half_adder_gates["b01"] = self.select(
            {self.carry_gates["c01"], "AND", self.x_and_y_gates["a01"]})
        for index in range(1, self.proper_length):
            i, j = f"{index:02}", f"{index + 1:02}"
            carry_and_digit_adder_i = self.select({
                self.carry_gates[f"c{i}"], "AND", self.x_xor_y_gates[f"s{i}"],
            })
            if carry_and_digit_adder_i != "Missing":
                next_carry = self.select({
                    carry_and_digit_adder_i, "OR", self.x_and_y_gates[f"a{i}"],
                })
                self.carry_and_half_adder_gates[f"b{i}"] = carry_and_digit_adder_i
                self.carry_gates[f"c{j}"] = next_carry
                continue
            raise NotImplementedError

    @cached_property
    def proper_length(self) -> int:
        initial_x = self.initial_number("x")
        initial_y = self.initial_number("y")
        proper_sum = bin(initial_x + initial_y)[2:]
        return len(proper_sum) - 1

    @staticmethod
    def _add_new_rule(rules: set[str], left:str, operation: str, right: str, result: str):
        rules.add(f"{left} {operation} {right} -> {result}")
        rules.add(f"{right} {operation} {left} -> {result}")

    @property
    def proper_rules(self) -> set[str]:
        rules = set()
        add_rule = partial(self._add_new_rule, rules)
        add_rule("x00", "AND", "y00", self.carry_gates["c01"])
        add_rule("x00", "XOR", "y00", "z00")
        for index in range(1, self.proper_length):
            i, j = f"{index:02}", f"{index + 1:02}"
            xi, yi, zi = f"x{i}", f"y{i}", f"z{i}"
            digit_adder_i = self.x_xor_y_gates[f"s{i}"]
            carry_i = self.carry_gates[f"c{i}"]
            carry_overflow_i = self.carry_and_half_adder_gates[f"b{i}"]
            digit_overflow_i = self.carry_and_half_adder_gates[f"a{i}"]
            next_carry = self.carry_gates[f"c{j}"]
            add_rule(xi, "XOR", yi, digit_adder_i)
            add_rule(xi, "AND", yi, digit_overflow_i)
            add_rule(digit_adder_i, "XOR", carry_i, zi)
            add_rule(digit_adder_i, "AND", carry_i, carry_overflow_i, )
            add_rule(digit_overflow_i, "OR", carry_overflow_i, next_carry)
        return rules

    @staticmethod
    def containing(string: str, words: set) -> bool:
        return set(string.split(" ")).issuperset(words)

    def select(self, words: set[str]) -> str:
        rule = [el for el in self.wrong_rules if self.containing(el, words)]
        if rule:
            return rule[0].split(" ")[4]
        return f"Missing"

    @property
    def find_wrong_rules(self) -> set[str]:
        return self.wrong_rules - self.proper_rules
