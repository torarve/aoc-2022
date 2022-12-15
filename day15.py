from common import read_lines
import re



lines = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".split("\n")

lines = read_lines("input15.txt")

sensors: list[tuple[int,int]] = []
beacons: list[tuple[int,int]] = []
for line in lines:
    m = re.match(r".*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)", line)
    sx, sy, bx, by = m.groups()
    sensors.append((int(sx), int(sy)))
    beacons.append((int(bx), int(by)))


line_y = 10
line_y = 2000000

def combine_ranges(r1, r2):
    if r1[0]>r2[0]: return combine_ranges(r2,r1)
    r1x1, r1x2 = r1
    r2x1, r2x2 = r2
    if r1x2 >= r2x1:
        return [(min(r1x1, r2x1), max(r1x2, r2x2))]

    return [r1, r2]


def find_overlap(line, sensors, beacons):
    range = None
    for i, (sx, sy) in enumerate(sensors):
        bx, by = beacons[i]
        d = abs(sx-bx) + abs(sy-by)

        w = d - abs(line_y - sy)
        if w >= 0: # Overlaps with line
            if range is None:
                range = (sx-w, sx+w)
            else:
                range = (min(range[0], sx-w), max(range[1], sx+w))
    return range

a, b = find_overlap(10, sensors, beacons)
print(b-a)

def merge(ranges, range):
    i = 0
    while i<len(ranges) and ranges[i][1] < range[0]-1:
        yield ranges[i]
        i += 1

    while i<len(ranges) and ranges[i][0] <= range[1]+1:
        range = (min(ranges[i][0], range[0]), max(ranges[i][1], range[1]))
        i += 1
    yield range

    while i<len(ranges):
        yield ranges[i]
        i += 1


upper_limit = 20
upper_limit = 4000000
for i in range(0,upper_limit+1):
    ranges = []
    for j, (sx, sy) in enumerate(sensors):
        bx, by = beacons[j]
        d = abs(sx-bx) + abs(sy-by)
        w = d - abs(i - sy)
        if w >= 0:
            range = (max(0, sx-w), min(sx+w, upper_limit))
            ranges = list(merge(ranges, range))

    if len(ranges)>1:
        x = ranges[0][1] + 1
        print(x*4000000 + i)
        break
    elif i % 1000 == 0:
        print(i)

                