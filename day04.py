from typing import Generator
from common import read_lines


def get_ranges(line: str) -> Generator[tuple[int, int], None, None]:
    for part in line.split(","):
        x, y = tuple(part.split("-"))
        yield (int(x), int(y))



lines = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8""".split("\n")

lines = read_lines("input04.txt")

def contains(first: tuple[int, int], second: tuple[int, int]):
    fx, fy = first
    sx, sy = second
    return fx <= sx and fy >= sy

def overlap(first: tuple[int, int], second: tuple[int, int]):
    fx, fy = first
    sx, sy = second
    return not (sy<fx or sx>fy)

count = 0
for line in lines:
    line_ranges = []
    for range in get_ranges(line):
        for prev_range in line_ranges:
            if contains(range, prev_range) or contains(prev_range, range):
                count += 1
        line_ranges.append(range)

print(count)


count = 0
for line in lines:
    line_ranges = []
    for range in get_ranges(line):
        for prev_range in line_ranges:
            if overlap(range, prev_range) or overlap(prev_range, range):
                count += 1
        line_ranges.append(range)

print(count)