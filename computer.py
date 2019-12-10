from dataclasses import dataclass, field
from typing import List

class Computer:
    def __init__(self, instruction_set, inputs=[], position = 0, input_position = 0):
        self.instruction_set = instruction_set
        self.position = position
        self.inputs = inputs
        self.input_position = input_position
        self.output = []
        self.stopped = False

    def process_all(self):
        while not self.stopped:
            self.process_one()

    def process_one(self):
        instruction = self.get_instruction()
        addr_values = self.evaluate_arg(instruction.args)
        if instruction.key_word == "add":
            addr_a = addr_values[0]
            addr_b = addr_values[1]
            self.instruction_set[instruction.output] = addr_a + addr_b
            self.position += 4
        elif instruction.key_word == "multiply":
            addr_a = addr_values[0]
            addr_b = addr_values[1]
            self.instruction_set[instruction.output] = addr_a * addr_b
            self.position += 4
        elif instruction.key_word == "input":
            while True:
                try:
                    next_input = self.inputs[self.input_position]
                    print("requested input got:", next_input)
                    break
                except ValueError:
                    print("Must be a number")
            self.instruction_set[instruction.output] = next_input
            self.input_position += 1
            self.position += 2
        elif instruction.key_word == "output":
            addr_a = addr_values[0]
            self.output.append(addr_a)
            self.position += 2
        elif instruction.key_word == "STOP":
            self.stopped = True
            if not self.output:
                self.output.append(self.instruction_set[0])
        else:
            raise Exception(f"Instruction not implemented {instruction.key_word}") 

    def evaluate_arg(self, args):
        addrs = []
        for arg in args:
            if arg.mode == "value":
                addrs.append(arg.value)
            elif arg.mode == "address":
                addrs.append(self.instruction_set[arg.value])
            else:
                raise Exception(f"Mode not implemented {arg.mode}") 
        return addrs

    def get_instruction(self):
        full_instruction = self.instruction_set[self.position]
        code = full_instruction % 100
        mode_names = ["address", "value"]
        modes = [
            full_instruction // 100 % 10, 
            full_instruction // 1000 % 10
        ]

        if code == 1:
            key_word = "add"
            args = [
                Arg(mode_names[modes[0]], self.instruction_set[self.position+1]),
                Arg(mode_names[modes[1]], self.instruction_set[self.position+2])
            ]
            output = self.instruction_set[self.position+3]
            return Instruction(key_word, args, output)
        elif code == 2:
            key_word = "multiply"
            args = [
                Arg(mode_names[modes[0]], self.instruction_set[self.position+1]),
                Arg(mode_names[modes[1]], self.instruction_set[self.position+2])
            ]
            output = self.instruction_set[self.position+3]
            return Instruction(key_word, args, output)
        elif code == 3:
            return Instruction(
                key_word = "input",
                output = self.instruction_set[self.position+1]
            )
        elif code == 4:
            return Instruction(
                key_word = "output",
                args = [Arg(mode_names[modes[0]], self.instruction_set[self.position+1])]
            )
        elif code == 99:
            return Instruction(key_word = "STOP")

        else:
            raise Exception(f"Instruction not implemented {code}") 

@dataclass
class Arg:
    mode: str
    value: int

@dataclass
class Instruction:
    key_word: str
    args: List[Arg] = field(default_factory=list)
    output: int = None

