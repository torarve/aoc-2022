lines = """1
2
-3
3
-2
0
4""".split("\n")

with open("input20.txt") as f:
    lines = [x.strip("\n") for x in f.readlines()]


def mix(values, indices, mod):
    for i, value in enumerate(values):
        if value == 0:
            continue
        current = indices[i]
        new = (current + value)%(mod-1)
        a, b = (current, new)
        if a < b:
            indices = [(x-1)%mod if x>=a and x<=b else x for x in indices]
        elif b < a:
            indices = [(x+1)%mod if x>=b and x<=a else x for x in indices]
        indices[i] = new

    return indices
        

values = [int(x) for x in lines]
mod = len(values)
indices = [x for x in range(0, mod)]
indices = mix(values, indices, mod)
values = [values[i] for i,x in sorted(enumerate(indices), key=lambda y: y[1])]
idx = values.index(0)

result = sum([values[(idx+1000)%mod],  values[(idx+2000)%mod], values[(idx+3000)%mod]])
print(result)


decryption_key = 811589153
values = [decryption_key*int(x) for x in lines]
indices = [x for x in range(0, mod)]
for i in range(0,10):
    indices = mix(values, indices, mod)

values = [values[i] for i,x in sorted(enumerate(indices), key=lambda y: y[1])]
idx = values.index(0)
result = sum([values[(idx+1000)%mod],  values[(idx+2000)%mod], values[(idx+3000)%mod]])
print(result)
