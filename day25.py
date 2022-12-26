from common import read_lines
import math

def find_representation(number):
    i = math.ceil(math.log(number,5))
    digits = []
    while 2*5**i < number:
        i += 1

    difference = number 
    i -= 1
    while i >= 0:
        weight = 5**i
        # minimize difference
        d = min([(x, abs(difference - x*weight)) for x in range(-2,3)], key=lambda t: t[1])[0]
        digits.append(d)
        difference -= d*weight
        i -= 1

    return "".join(["012=-"[x] for x in digits])


lines = """1=-0-2
12111
2=0=
21
2=01
111
20012
112
1=-1=
1-12
12
1=
122""".split("\n")

lines = read_lines("input25.txt")

weights = { "2": 2, "1": 1, "0": 0, "-": -1, "=": -2 }
value = sum([sum([(5**i) * weights[x] for i, x in enumerate(reversed(line))]) for line in lines])

number = find_representation(value)
print(f"{value} => {number}")

