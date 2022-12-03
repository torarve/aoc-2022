from common import read_lines


def calculate_score(a, b):
    score = 1 if b == "X" else 2 if b == "Y" else 3

    if a == "A" and b == "X": score += 3
    if a == "A" and b == "Y": score += 6
    if a == "B" and b == "Y": score += 3
    if a == "B" and b == "Z": score += 6
    if a == "C" and b == "Z": score += 3
    if a == "C" and b == "X": score += 6

    return score

def choose_play(a, b):
    if a == "A" and b == "X": return "Z"
    if a == "A" and b == "Y": return "X"
    if a == "A" and b == "Z": return "Y"

    if a == "B" and b == "X": return "X"
    if a == "B" and b == "Y": return "Y"
    if a == "B" and b == "Z": return "Z"

    if a == "C" and b == "X": return "Y"
    if a == "C" and b == "Y": return "Z"
    if a == "C" and b == "Z": return "X"

lines = read_lines("input02.txt")
hands = [tuple(line.split(" ")) for line in lines]

part1 = sum([calculate_score(a, b) for (a,b) in hands])
print(f"Answer part 1: {part1}")
part2 = sum([calculate_score(a, choose_play(a, b)) for (a, b) in hands])
print(f"Answer part 2: {part2}")
