def read_files() -> list[str]:
    with open("input01.txt") as f:
        return [x.strip() for x in f.readlines()]

test_input = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

lines = test_input.split("\n")

lines = read_files()

sum = 0
sums = []
for line in lines:
    if line == "":
        sums.append(sum)
        sum = 0
    else:
        sum += int(line)

print(f"Answer part 1: {max(sums)}")
sums.sort()
print(f"Answer part 2: {sums[-3]+sums[-2]+sums[-1]}")