from math import lcm
from common import read_lines


class Monkey():
    def __init__(self):
        self.items = []
        self.op = ("+", 0)
        self.test = 0
        self.true = -1
        self.false = -1
        self.inspection_count = 0

    def calculate_worry_level(self, item, part1=True):
        what, value = self.op
        value = item if value == "old" else int(value)

        if what == "+":
            value = item + value
        elif what == "*":
            value = item * value

        if part1:
            value //= 3

        return value

    def inspect(self, item, part1):
        self.inspection_count += 1
        level = self.calculate_worry_level(item, part1)
        if level % self.test == 0:
            return self.true, level

        return self.false, level

    def __repr__(self):
        return f"Monkey({self.items}, {self.op}, {self.test}, {self.true}, {self.false})"


def parse(lines: list[str]) -> list[Monkey]:
    monkeys = []

    for line in lines:
        line = line.strip()
        if line.startswith("Monkey"):
            monkeys.append(Monkey())
        if line.startswith("Starting items: "):
            monkeys[-1].items = [int(x)
                                 for x in line[len("Starting items: "):].split(", ")]
        if line.startswith("Operation: new = old "):
            tmp = line[len("Operation: new = old "):].split(" ")
            monkeys[-1].op = (tmp[0], tmp[1])
        if line.startswith("Test: divisible by "):
            monkeys[-1].test = int(line[len("Test: divisible by "):])
        if line.startswith("If true: throw to monkey "):
            monkeys[-1].true = int(line[len("If true: throw to monkey "):])
        if line.startswith("If false: throw to monkey "):
            monkeys[-1].false = int(line[len("If false: throw to monkey "):])

    return monkeys


def step(monkeys: list[Monkey], step1: bool = True, mod: int = 0):
    for monkey in monkeys:
        for item in monkey.items:
            next_monkey, new_item = monkey.inspect(item, step1)
            if mod > 0:
                new_item %= mod

            monkeys[next_monkey].items.append(new_item)

        monkey.items = []


def run(lines: list[str], part1: bool) -> int:
    monkeys = parse(lines)
    mod = lcm(*[x.test for x in monkeys])
    count = 20 if part1 else 10000
    for i in range(0, count):
        step(monkeys, part1, mod)
    top_2 = sorted([x.inspection_count for x in monkeys])[-2:]
    return (top_2[-1] * top_2[-2])


lines = read_lines("input11.txt")
print(f"Answer part 1: {run(lines, True)}")
print(f"Anwser part 2: {run(lines, False)}")
