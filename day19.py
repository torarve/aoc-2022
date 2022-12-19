from common import read_lines
import re

class Blueprint:
    def __init__(self, id):
        self.id = id
        self.lines: dict[str,dict[str,int]] = {}

    def __repr__(self):
        return f"Blueprint({self.id})"

lines = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.""".split("\n")

lines = read_lines("input19.txt")
blueprints: list[Blueprint] = []


for line in lines:
    tmp = line.split(": ")
    id = int(tmp[0][10:])
    blueprint = Blueprint(id)
    for tmp2 in tmp[1].split(". "):
        m = re.match(r"Each (\w+) robot costs (.+)", tmp2)
        type = m.group(1)
        costs = dict([(name, int(cost)) 
            for cost, name in [tuple(t.split(" ")) 
                for t in m.group(2).strip(".").split(" and ")]])
        blueprint.lines[type] = costs

    blueprints.append(blueprint)

max_required_of = {}
for k, v in [x for _, y in blueprint.lines.items() for x in y.items()]:
    max_required_of[k] = max(max_required_of.get(k,-1), v)


def step(remaining: int, blueprint: Blueprint, robots: dict[str,int], wallet: dict[str,int], seen, best_answer = 0):
    upper_limit = wallet["geode"] + robots["geode"]*remaining + ((remaining+1)*remaining)//2
    if upper_limit <= best_answer:
        return -1

    state = hash(f"{robots}|{wallet}|{remaining}")
    if state in seen:
        return seen[state]

    if remaining == 0:
        return wallet["geode"]

    can_build = []
    for type, cost in blueprint.lines.items():
        if all([wallet[cost_item]>=cost_value for cost_item, cost_value in cost.items()]):
            # Choose: build or not?
            can_build.append(type)

    # Update current wallet based on available robots
    for type, count in robots.items():
        wallet[type] += count

    best_value = wallet["geode"]
    # Create new robot if possible
    for to_build in can_build:
        if to_build != "geode":
            if max_required_of[to_build]*remaining <= wallet[to_build]:
                continue

            # No need to build more of a robot if we never will be able to use it
            if max_required_of[to_build] <= robots[to_build]:
                continue

        new_wallet = dict(x for x in wallet.items())
        new_robots = dict(x for x in robots.items())
        for type, value in blueprint.lines[to_build].items():
            new_wallet[type] -= value
        new_robots[to_build] += 1
        best_value = max(best_value, step(remaining-1, blueprint, new_robots, new_wallet, seen, max(best_value, best_answer)))

    best_value = max(best_value, step(remaining-1, blueprint, robots, wallet, seen, max(best_value, best_answer)))        
    seen[state] = best_value
    return best_value


values = []
for blueprint in blueprints:
    opened_geodes = step(24, blueprint, { "ore": 1, "clay": 0, "obsidian": 0, "geode": 0}, { "ore": 0, "clay": 0, "obsidian": 0, "geode": 0}, {})
    print(opened_geodes)
    values.append(opened_geodes*blueprint.id)

print(sum(values))

values = []
for blueprint in blueprints[:3]:
    opened_geodes = step(32, blueprint, { "ore": 1, "clay": 0, "obsidian": 0, "geode": 0}, { "ore": 0, "clay": 0, "obsidian": 0, "geode": 0}, {})
    print(opened_geodes)
    values.append(opened_geodes)

print(values[0]*values[1]*values[2])
