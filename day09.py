from common import read_lines

def parse(line: str) -> tuple[int, str]:
    """Parse single line"""
    tmp = line.split(" ")
    return tmp[0], int(tmp[1])

def move_head(head: tuple[int, int], direction: str) -> tuple[int,int]:
    """Move the first knot one step in the given direction."""
    x, y = head
    if direction == "U":
        return (x, y+1)
    elif direction == "D":
        return (x, y-1)
    elif direction == "L":
        return (x-1, y)
    elif direction == "R":
        return (x+1, y)

def update_tail(head: tuple[int, int], tail: tuple[int, int]) -> tuple[int, int]:
    """Update position of knot based on previous knot"""
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

def simulate(steps: list[str], size: int):
    knots = [(0,0)] * size
    tail_positions = set()
    for line in steps:
        direction, steps = parse(line)
        for i in range(1, steps+1):
            knots[0] = move_head(knots[0], direction)
            for i in range(1, size):
                knots[i] = update_tail(knots[i-1], knots[i])
            
            tail_positions.add(knots[-1])

    return len(tail_positions)


steps = read_lines("input09.txt")
print(f"Answer to part 1: {simulate(steps, 2)}")
print(f"Answer to part 2: {simulate(steps, 10)}")
