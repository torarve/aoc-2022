
from pprint import pprint
import sympy
from sympy.abc import x
import re

from common import read_lines

def evaluate(name, monkeys):
    if isinstance(monkeys[name], int):
        return monkeys[name]
    else:
        a, op, b = monkeys[name]
        a = evaluate(a, monkeys)
        b = evaluate(b, monkeys)
        return eval(f"int({a}{op}{b})")


lines = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32""".split("\n")

lines = read_lines("input21.txt")

monkeys = {}
for line in lines:
    name, op = line.split(": ")
    if re.match("\d+", op):
        monkeys[name] = int(op)
    else:
        a = op[:4]
        b = op[5]
        c = op[7:]
        monkeys[name] = (a, b, c)


class Expression:

    def __init__(self, lhs, rhs, op: str):
        self.lhs = lhs
        self.rhs = rhs
        self.op = op

    def __repr__(self):
        lhs = f"({self.lhs})" if isinstance(self.lhs, Expression) else self.lhs
        rhs = f"({self.rhs})" if isinstance(self.rhs, Expression) else self.rhs
        return f"{lhs}{self.op}{rhs}"

    def simplify(self):
        # x + 1
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __div__(self, other):
        pass

def evaluate2(name, monkeys):
    if name == "humn":
        return "x"
    elif isinstance(monkeys[name], int):
        return monkeys[name]
    else:
        a, op, b = monkeys[name]
        a = evaluate2(a, monkeys)
        b = evaluate2(b, monkeys)
        op = " = " if name == "root" else op
        if isinstance(a, int) and isinstance(b, int):
            return eval(f"int({a}{op}{b})")
        else:
            return Expression(a, b, op)

def solve(a, b):
    if isinstance(a, int) or isinstance(a, float): return solve(b, a)
    if isinstance(a, str):
        # Solution found
        return int(b)

    lhs, rhs = a.lhs, a.rhs
    # lhs is always expression or string
    if isinstance(lhs, int) or isinstance(lhs, float):
        match a.op:
            case "+": return solve(b-lhs, rhs)
            case "-": return solve(b+lhs, rhs)
            case "*": return solve(b/lhs, rhs)
            case "/": return solve(b*lhs, rhs)
    else:
        match a.op:
            case "+": return solve(lhs, b-rhs)
            case "-": return solve(lhs, b+rhs)
            case "*": return solve(lhs, b/rhs)
            case "/": return solve(lhs, b*rhs)
    

def evaluate3(name, monkeys):
    if name == "humn":
        return x
    elif isinstance(monkeys[name], int):
        return monkeys[name]
    else:
        a, op, b = monkeys[name]
        a = evaluate3(a, monkeys)
        b = evaluate3(b, monkeys)
        if name == "root":
            raise "Error"
        match op:
            case "+": return a + b
            case "-": return a - b
            case "*": return a * b
            case "/": return a / b
        
# print(solve(a, b))
# expr = str(evaluate2("root", monkeys))
# print(expr)
a, _, b = monkeys["root"]
a, b = evaluate2(a, monkeys), evaluate2(b, monkeys)
print(solve(a,b))

# # Solve using SymPy
# monkeys["humn"] = x
# a, _, b = monkeys["root"]
# a, b = evaluate3(a, monkeys), evaluate3(b, monkeys)
# print(sympy.solve(a-b, x))

# pprint(monkeys)

# 8578625219205
# 206172047007866.0 - 9625*x/288 80526799293735.0
# [3759566892641.01]