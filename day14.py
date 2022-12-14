from common import read_lines


def point_range(begin, end):
    x1, y1 = begin
    x2, y2 = end
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2)+1):
            yield (x1, i)
    else:
        for i in range(min(x1, x2), max(x1, x2)+1):
            yield (i, y1)


def init(lines):
    blocked = set()
    for line in lines:
        points = [eval(x) for x in line.split(" -> ")]
        for i in range(1, len(points)):
            for x in point_range(points[i-1], points[i]):
                blocked.add(x)

    return blocked


def next_position(x, y, blocked):
    if (x, y+1) not in blocked:
        return x, y + 1
    elif (x-1, y+1) not in blocked:
        return x-1, y+1
    elif (x+1, y+1) not in blocked:
        return (x+1, y+1)
    return None


def run(lines, part1: bool = True, should_print: bool = False):
    path = []
    blocked = init(lines)
    count = 0
    if part1:
        bottom = max([y for x, y in blocked])
    else:
        bottom = max([y for x, y in blocked]) + 2
    x, y = (500, 0)

    while (part1 and y <= bottom) or (not part1 and (x, y) not in blocked):
        path.append((x, y))
        next = next_position(x, y, blocked)
        if next is not None and (part1 or next[1] < bottom):
            x, y = next
        else:
            blocked.add((x, y))
            path = []
            count += 1
            x, y = (500, 0)

    if should_print:
        rocks = init(lines)
        xmin, xmax, ymin, ymax = min([x for x, y in blocked]), max(
            [x for x, y in blocked]), 0, max([y for x, y in blocked])
        w = (xmax-xmin)+1
        output = [' ']*w*(ymax-ymin+1)
        for x, y in blocked:
            output[(x-xmin) + y*w] = '*'
        for x, y in rocks:
            output[(x-xmin) + y*w] = '#'
        for x, y in path:
            output[(x-xmin) + y*w] = '¤'

        for y in range(ymin, ymax+1):
            print("".join(output[y*w:(y+1)*w]))

    return count


lines = read_lines("input14.txt")
print(f"Answer part 1: {run(lines, True, should_print=True)}")
print(f"Answer part 2: {run(lines, False, should_print=False)}")
