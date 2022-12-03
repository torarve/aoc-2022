from common import read_lines


def score(char: str) -> int:
    if char.isupper():
        return ord(char)-ord('A')+27
    return ord(char)-ord('a')+1

def check_part1(lines: str) -> int:
    for line in lines:
        part1, part2 = line[:len(line)//2], line[len(line)//2:]
        common = set([x for x in part1 if x in part2])
        yield [score(x) for x in common][0]

def split_for_part2(lines: list[str]) -> list[str]:
    for i in range(0, len(lines)-1, 3):
        yield lines[i:i+3]

def check_part2(lines: list[str]) -> int:
    for group in split_for_part2(lines):
        result = None
        for line in group:
            if result is None:
                result = set([x for x in line])
            else:
                result = set([x for x in result if x in line])
        yield [score(x) for x in result][0]

lines = read_lines("input03.txt")

print(f"Answer part 1: {sum(check_part1(lines))}")
print(f"Answer part 2: {sum(check_part2(lines))}")