from collections import deque
from functools import reduce

from common import read_lines


lines = """....#..
..###.#
#...#.#
.#...##
#.###..
##.#.##
.#..#..""".split("\n")


# lines = """.....
# ..##.
# ..#..
# .....
# ..##.
# .....""".split("\n")

lines = read_lines("input23.txt")

# If there is no Elf in the N, NE, or NW adjacent positions, the Elf proposes moving north one step.
# If there is no Elf in the S, SE, or SW adjacent positions, the Elf proposes moving south one step.
# If there is no Elf in the W, NW, or SW adjacent positions, the Elf proposes moving west one step.
# If there is no Elf in the E, NE, or SE adjacent positions, the Elf proposes moving east one step.

elves: list[tuple[int,int]] = []
for y in range(0, len(lines)):
    for x in range(0, len(lines[y])):
        if lines[y][x] == "#":
            elves.append((int(x), int(y)))

def bounds(elves):
    xmin, ymin = elves[0]
    xmax, ymax = elves[0]
    for x, y in elves[1:]:
        xmin, ymin = min(xmin, x), min(ymin, y)
        xmax, ymax = max(xmax, x), max(ymax, y)
    return xmin, ymin, xmax, ymax


def show_map(elves):
    left, top, right, bottom = bounds(elves)
    left, top, right, bottom = left -1, top -1, right + 1, bottom + 1
    w = right - left + 1
    h = bottom - top + 1
    for y in range(top-1, bottom + 1):
        l = "".join(["#" if (x,y) in elves else "."
            for x in range(left-1, right+1)])
        print(l)




def round(round_number: int, elves: list[tuple[int,int]]):
    proposals: list[tuple[int,int]] = [None] * len(elves)
    for i, (x, y) in enumerate(elves):
        nw, n, ne = (x-1, y-1), (x, y-1), (x+1, y-1)
        w, e = (x-1, y), (x+1, y)
        sw, s, se = (x-1, y+1), (x, y+1), (x+1, y+1)
        tmp = [ nw in elves, n in elves, ne in elves, 
                w in elves, False, e in elves,
                sw in elves, s in elves, se in elves]
        if any(tmp):
            checks = deque([None if any(tmp[0:3]) else n, 
                None if any(tmp[6:]) else s,
                None if any(tmp[0::3]) else w,
                None if any(tmp[2::3]) else e])
            checks.rotate(-(round_number%4))
            while len(checks) > 0 and checks[0] is None:
                checks.popleft()
            if len(checks) > 0:
                proposals[i] = checks[0]

    seen, duplicates = set(), set()
    for p in proposals:
        if p in seen:
            duplicates.add(p)
        elif p is not None:
            seen.add(p)

    return [p if p is not None and p not in duplicates else elves[i]
        for i, p in enumerate(proposals)], len(seen)-len(duplicates)
        


print(elves)
print()
show_map(elves)
print()

for i in range(0, 10):
    elves, moved = round(i, elves)
    print(f"Round {i+1}")
    # show_map(elves)
    # print()

left, top, right, bottom = bounds(elves)
result = sum([0 if (x,y) in elves else 1 
    for x in range(left, right+1)
        for y in range(top, bottom+1)])
print(result)

while moved>0:
    i = i + 1
    elves, moved = round(i, elves)
    print(f"Round {i+1}")
    print(moved, bounds(elves))

print(i+1)