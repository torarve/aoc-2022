from itertools import accumulate
from typing import Callable, Generator, Iterable
from common import read_lines

class Range:
    @staticmethod
    def parse(rangeStr: str) -> "Range":
        a, b = tuple(rangeStr.split("-"))
        return Range(int(a), int(b))

    @staticmethod
    def parse_line(line: str) -> Generator["Range", None, None]:
        for part in line.split(","):
            yield Range.parse(part)

    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def contains(self, other: "Range") -> bool:
        return self.start <= other.start and self.end >= other.end

    def overlaps(self, other: "Range") -> bool:
        return not (other.end<self.start or other.start>self.end)


def count_matches(ranges: Iterable[Range], f: Callable[[Range, Range], bool]) -> int:
    result = 0
    prev: list[Range] = []
    for range in ranges:
        result += sum([1 for x in prev if f(range, x) or f(x, range)])
        prev.append(range)
    return result


lines = read_lines("input04.txt")
range_sets = [list(Range.parse_line(line)) for line in lines]

answer = sum([count_matches(x, Range.contains) for x in range_sets])
print(f"Answer part 1: {answer}")

answer = sum([count_matches(x, Range.overlaps) for x in range_sets])
print(f"Answer part 2: {answer}")
