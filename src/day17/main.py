import re
from enum import Enum
from pathlib import Path
from typing import Optional

from icecream import ic


class OpCodes(Enum):
    adv = 0
    bxl = 1
    bst = 2
    jnz = 3
    bxc = 4
    out = 5
    bdv = 6
    cdv = 7


class Program:
    def __init__(
        self, data: list[str] = None, A=None, B=None, C=None, instructions=None
    ):
        _pattern = re.compile(r"\d+")
        self.register_A = int(_pattern.findall(data[0])[0]) if data else A
        self.register_B = int(_pattern.findall(data[1])[0]) if data else B
        self.register_C = int(_pattern.findall(data[2])[0]) if data else C
        self._instructions = (
            re.compile(r"Program: ([\d,]+)").findall(data[4])[0]
            if data
            else instructions
        )
        self.instructions = [int(char) for char in self._instructions if char != ","]
        self.pointer = 0
        self.output = []

    def run(self) -> str:
        while self.pointer < len(self.instructions):
            opcode = self.instructions[self.pointer]
            operand = self.instructions[self.pointer + 1]
            op = getattr(self, OpCodes(opcode).name)
            output = op(operand)
            if output:
                self.output.append(output)
            if opcode != OpCodes.jnz.value:
                self.pointer += 2
            self.run()
        return ",".join(self.output)

    def combo(self, operand):
        match operand:
            case s if s in {0, 1, 2, 3}:
                return s
            case 4:
                return self.register_A
            case 5:
                return self.register_B
            case 6:
                return self.register_C
            case 7:
                pass

    def _division(self, operand) -> int:
        return self.register_A // (2 ** self.combo(operand))

    def adv(self, operand):
        division = self._division(operand)
        self.register_A = division
        return None

    def bxl(self, operand):
        xor = self.register_B.__xor__(operand)
        self.register_B = xor
        return None

    def bst(self, operand):
        module = self.combo(operand) % 8
        self.register_B = module
        return None

    def jnz(self, operand):
        if self.register_A == 0:
            self.pointer += 2
            return
        self.pointer = operand
        return None

    def bxc(self, operand):
        _ = operand
        xor = self.register_B.__xor__(self.register_C)
        self.register_B = xor
        return None

    def out(self, operand):
        modulo = self.combo(operand) % 8
        return str(modulo)

    def bdv(self, operand):
        division = self._division(operand)
        self.register_B = division
        return None

    def cdv(self, operand):
        division = self._division(operand)
        self.register_C = division
        return None

    def revert(self):
        pass


class Solution:
    _STANDARD_PATH = Path(__file__).parent / "input.txt"

    def __init__(self, path: Path = _STANDARD_PATH, lines: Optional[list[str]] = None):
        with open(path) as file:
            self.lines = file.readlines() if not lines else lines

    def first_task(self) -> str:
        pc = Program(self.lines)
        return pc.run()

    def second_task(self) -> int:
        pc = Program(self.lines)
        answer = 0
        while pc._instructions != ",".join(pc.output):
            pc = Program(A=answer, B=0, C=0, instructions=pc.instructions)
            ic(pc.run())
            answer += 1
        return answer


def main():
    solution = Solution()
    print("The first answer is", solution.first_task())
    print("The second answer is", solution.second_task())


if __name__ == "__main__":
    main()
