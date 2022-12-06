from common import read_lines


def find_marker(input: str, marker_size = 4) -> int:
    def sum_chars(line: str) -> dict[str,int]:
        res = {}
        for c in line:
            if c in res:
                res[c] += 1
            else:
                res[c] = 1
        return res
    for i in range(0, len(input)-marker_size):
        counts = sum_chars(input[i:i+marker_size])
        if all([x==1 for x in counts.values()]):
            return i+marker_size


input = read_lines("input06.txt")[0]

print(f"Answer part 1: {find_marker(input, 4)}")
print(f"Answer part 1: {find_marker(input, 14)}")
