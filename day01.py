from typing import Generator
from common import read_lines

def count_calories(lines: list[str]) -> Generator[int, None, None]:
    sum = 0
    for line in lines:
        if line == "":
            yield sum
            sum = 0
        else:
            sum += int(line)

sums = sorted(count_calories(read_lines("input01.txt")))
print(f"Answer part 1: {max(sums)}")
print(f"Answer part 2: {sum(sums[-3:])}")