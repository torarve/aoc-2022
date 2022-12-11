from common import read_lines


lines = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1""".split("\n")

lines = read_lines("input11.txt")

class Monkey():
    def __init__(self):
        self.items = []
        self.op = ("+", 0)
        self._op = None
        self.test = 0
        self.true = -1
        self.false = -1
        self.inspection_count = 0

    def worry(self, item):
        what, value = self.op
        if value == "old":
            value = item
        else:
            value = int(value)

        if what == "+":
            return item + value
        elif what == "*":
            return item * value

    def __repr__(self):
        return f"Monkey({self.items}, {self.op}, {self.test}, {self.true}, {self.false})"


class Monkey2:
    def __init__(self):
        self.items: list[tuple[int,int]] = []
        self.op = ("+", 0)
        self.test = 0
        self.true = -1
        self.false = -1
        self.inspection_count = 0

    def worry(self, item: list[tuple[int,int]]):
        what, value = self.op
        if value == "old":
            return [((x * x) % y, y) for x,y in item]

        value = int(value)
        if what == "+":
            return [(x + value % y, y) for x,y in item]
        elif what == "*":
            return [((x * value) % y, y) for x,y in item]

def parse(lines: list[str]) -> list[Monkey]:
    monkeys = []

    for line in lines:
        line = line.strip()
        if line.startswith("Monkey"):
            monkeys.append(Monkey())
        if line.startswith("Starting items: "):
            monkeys[-1].items = [int(x) for x in line[len("Starting items: "):].split(", ")]
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

def step(monkeys: list[Monkey], step1: bool = True):
    for monkey in monkeys:
        for item in monkey.items:
            level = monkey.worry(item)
            if step1:
                level = level // 3
            if level % monkey.test == 0:
                monkeys[monkey.true].items.append(level)
            else: 
                monkeys[monkey.false].items.append(level)
            monkey.inspection_count += 1
    
        monkey.items = []


def step2(monkeys: list[Monkey2]):
    for i, monkey in enumerate(monkeys):
        for item in monkey.items:
            level = monkey.worry(item)
            if level[i][0] % monkey.test == 0:
                monkeys[monkey.true].items.append(level)
            else: 
                monkeys[monkey.false].items.append(level)
            monkey.inspection_count += 1
    
        monkey.items = []

monkeys = parse(lines)
for i in range(0, 20):
    step(monkeys, True)
top_2 = sorted([x.inspection_count for x in monkeys])
print(top_2[-1] * top_2[-2])

monkeys = parse(lines)
divisors = [x.test for x in monkeys]
monkeys2 = []
for monkey in monkeys:
    m = Monkey2()
    m.items = [[(item % x, x) for x in divisors] for item in monkey.items]
    m.op = monkey.op
    m.test = monkey.test
    m.true = monkey.true
    m.false = monkey.false
    monkeys2.append(m)

for i in range(0, 10000):
    step2(monkeys2)
top_2 = sorted([x.inspection_count for x in monkeys2])
print(top_2[-1] * top_2[-2])
