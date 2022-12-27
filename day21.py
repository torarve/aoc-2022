import re
from common import read_lines


def evaluate(name, monkeys):
    monkey = monkeys[name]
    if isinstance(monkey, int) or isinstance(monkey, str):
        return monkey
    else:
        a, op, b = monkey
        a = evaluate(a, monkeys)
        b = evaluate(b, monkeys)
        if isinstance(a, int) and isinstance(b, int):
            return int(eval(f"{a}{op}{b}"))
        else:
            return (a, op, b)


def solve(a, b: int):
    if isinstance(a, int) or isinstance(a, float): return solve(b, a)
    if isinstance(a, str):
        # Solution found
        return int(b)

    lhs, op, rhs = a
    # lhs is always expression or string
    if isinstance(lhs, int) or isinstance(lhs, float):
        match op:
            case "+": return solve(b-lhs, rhs)
            case "-": return solve(lhs-b, rhs)
            case "*": return solve(b/lhs, rhs)
            case "/": return solve(lhs/b, rhs)
    else:
        match op:
            case "+": return solve(lhs, b-rhs)
            case "-": return solve(lhs, b+rhs)
            case "*": return solve(lhs, b/rhs)
            case "/": return solve(lhs, b*rhs)


monkeys = {}
for line in read_lines("input21.txt"):
    name, op = line.split(": ")
    if re.match("\d+", op):
        monkeys[name] = int(op)
    else:
        a = op[:4]
        b = op[5]
        c = op[7:]
        monkeys[name] = (a, b, c)

        
print(f"Solution part1: {evaluate('root', monkeys)}")
monkeys["humn"] = "x"
a, _, b = monkeys["root"]
a, b = evaluate(a, monkeys), evaluate(b, monkeys)
print(f"Solution part 2: {solve(a,b)}")
