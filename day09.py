from common import read_lines


steps="""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".split("\n")

steps = read_lines("input09.txt")

def parse(line: str) -> tuple[int, str]:
    tmp = line.split(" ")
    return tmp[0], int(tmp[1])

def update_tail(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    hx, hy = head
    tx, ty = tail
    if hx > tx + 1:
        tx = tx + 1
        if hy > ty:
            ty += 1
        elif hy < ty:
            ty -= 1
    elif hx + 1 < tx:
        tx = tx - 1
        if hy > ty:
            ty += 1
        elif hy < ty:
            ty -= 1
    elif hy > ty + 1:
        ty = ty + 1
        if hx > tx:
            tx += 1
        elif hx < tx:
            tx -= 1
    elif hy + 1 < ty:
        ty = ty - 1
        if hx > tx:
            tx += 1
        elif hx < tx:
            tx -= 1

    return tx, ty

def simulate_part1(steps: list[str]):
    head = (0,0)
    tail = (0,0)
    tail_positions = set()
    for line in steps:
        direction, steps = parse(line)
        for i in range(1, steps+1):
            x, y = head
            if direction == "U":
                head = (x, y+1)
            elif direction == "D":
                head = (x, y-1)
            elif direction == "L":
                head = (x-1, y)
            elif direction == "R":
                head = (x+1, y)

            tail = update_tail(head, tail)
            tail_positions.add(tail)

    return len(tail_positions)


def simulate_part2(steps: list[str]):
    head = (0,0)
    tails: list[tuple[int, int]] = [(0,0)] * 9
    tail_positions = set()
    for line in steps:
        direction, steps = parse(line)
        for i in range(1, steps+1):
            x, y = head
            if direction == "U":
                head = (x, y+1)
            elif direction == "D":
                head = (x, y-1)
            elif direction == "L":
                head = (x-1, y)
            elif direction == "R":
                head = (x+1, y)

            tails[0] = update_tail(head, tails[0])
            for i in range(0, 8):
                tails[i+1] = update_tail(tails[i], tails[i+1])
            
            tail_positions.add(tails[-1])

    return len(tail_positions)

print(simulate_part1(steps))
print(simulate_part2(steps))