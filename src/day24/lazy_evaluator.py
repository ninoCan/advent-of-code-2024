import re
from dataclasses import dataclass


class LazyEvaluator:
    def __init__(self, data: list[str]):
        wire_pattern = re.compile(r'(\w\d\d): (\d)')
        empty_line_index = data.index("\n")
        self.wires: dict[str, int] = {}
        for line in data[:empty_line_index]:
            if match:=wire_pattern.findall(line):
                wire, value = match[0]
                self.wires[wire] = int(value)
        gate_pattern = re.compile(r'\w+')
        self.gates: dict[str, Gate] = dict()
        for line in data[empty_line_index + 1:]:
            if match:=gate_pattern.findall(line):
                left, operator_str, right, gate_name = match
                self.gates[gate_name] = Gate(left, right, operator=operator_str)

    @property
    def final_number(self) -> int:
        self.elaborate()
        zeds = [
            self.wires[key]
            for key in sorted(self.gates.keys())
            if key.startswith("z")
        ]
        return sum([value * 2 ** idx for idx, value in enumerate(zeds)])

    def initial_number(self, addee: str) -> int:
        if addee not in {"x", "y"}:
            raise ValueError(f"Invalid addee: {addee}. Must be 'x' or 'y'")
        digits = [
            self.wires[key]
            for key in sorted(self.wires.keys())
            if key.startswith(addee)
        ]
        return sum([value * 2 ** idx for idx, value in enumerate(digits)])


    def elaborate(self):
        initial_wires = len(self.wires.keys())
        while len(self.wires.keys()) != len(self.gates.keys()) + initial_wires:
            for addr, gate in self.gates.items():
                if gate.can_be_evaluated(self.wires) and addr not in self.wires.keys():
                    gate.evaluate(self.wires)
                    self.wires[addr] = gate.result


@dataclass
class Gate:
    left: str
    right: str
    operator: str
    result = None


    @property
    def is_evaluated(self) -> bool:
        return True if self.result else False

    def can_be_evaluated(self, wires: dict[str, int]) -> bool:
        return {self.left, self.right}.issubset(set(wires.keys()))

    def evaluate(self, wires: dict[str, int]):
        match self.operator:
            case "AND":
                self.result = wires[self.left] & wires[self.right]
            case "OR":
                self.result = wires[self.left] | wires[self.right]
            case "XOR":
                self.result = wires[self.left] ^ wires[self.right]
